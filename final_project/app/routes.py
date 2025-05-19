from app.models import Autor  # asegúrate de importarlo arriba
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.forms import LibroForm, ChangePasswordForm, PrestamoForm
from app.models import db, Libro, User, Prestamo
from app.models import Autor
# Blueprint principal que maneja el dashboard, gestión de libros y cambio de contraseña
main = Blueprint('main', __name__)


@main.route('/')
def index():
    """
    Página de inicio pública (home).
    """
    return render_template('index.html')


@main.route('/cambiar-password', methods=['GET', 'POST'])
@login_required
def cambiar_password():
    """
    Permite al usuario autenticado cambiar su contraseña.
    """
    form = ChangePasswordForm()

    if form.validate_on_submit():
        # Verifica que la contraseña actual sea correcta
        if not current_user.check_password(form.old_password.data):
            flash('La contraseña actual es incorrecta.')
            return render_template('cambiar_password.html', form=form)

        # Actualiza la contraseña y guarda
        current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('Contraseña actualizada correctamente.')
        return redirect(url_for('main.dashboard'))

    return render_template('cambiar_password.html', form=form)


@main.route('/dashboard')
@login_required
def dashboard():
    """
    Panel principal del usuario. Muestra los libros si no es lector.
    """
    if current_user.role.name == 'Lector':  # Solo los lectores ven los libros disponibles
        libros = Libro.query.filter_by(disponible=True).all()
    else:
        libros = Libro.query.all()  # Admin y bibliotecarios pueden ver todos los libros

    return render_template('dashboard.html', libros=libros)


@main.route('/libros', methods=['GET', 'POST'])
@login_required
def crear_libro():
    form = LibroForm()
    if form.validate_on_submit():
        # Buscar o crear autor
        nombre_autor = form.autor.data.strip()
        autor_obj = Autor.query.filter_by(nombre=nombre_autor).first()
        if not autor_obj:
            autor_obj = Autor(nombre=nombre_autor)
            db.session.add(autor_obj)
            db.session.commit()  # necesario para obtener id

        libro = Libro(
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            autor_id=autor_obj.id,
            disponible=form.disponible.data,
            isbn=form.isbn.data
        )

        db.session.add(libro)
        db.session.commit()
        flash("Libro creado exitosamente.")
        return redirect(url_for('main.dashboard'))

    return render_template('libro_form.html', form=form)


@main.route('/libros/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_libro(id):
    """
    Permite editar un libro existente. Solo si es admin o bibliotecario.
    """
    libro = Libro.query.get_or_404(id)

    # Validación de permisos
    if current_user.role.name not in ['Admin', 'Bibliotecario']:
        flash('No tienes permiso para editar este libro.')
        return redirect(url_for('main.dashboard'))

    form = LibroForm(obj=libro)

    if form.validate_on_submit():
        libro.titulo = form.titulo.data
        libro.descripcion = form.descripcion.data
        libro.autor = Autor.query.get(
            form.autor.data)  # ← Esto es una instancia
        db.session.commit()
        flash("Libro actualizado exitosamente.")
        return redirect(url_for('main.dashboard'))

    return render_template('libro_form.html', form=form, editar=True)


@main.route('/libros/<int:id>/eliminar', methods=['POST'])
@login_required
def eliminar_libro(id):
    """
    Elimina un libro si el usuario es admin o bibliotecario.
    """
    libro = Libro.query.get_or_404(id)

    if current_user.role.name not in ['Admin', 'Bibliotecario']:
        flash('No tienes permiso para eliminar este libro.')
        return redirect(url_for('main.dashboard'))

    db.session.delete(libro)
    db.session.commit()
    flash("Libro eliminado exitosamente.")
    return redirect(url_for('main.dashboard'))


@main.route('/prestamos', methods=['GET', 'POST'])
@login_required
def prestamos():
    """
    Permite registrar un préstamo de libro. Solo disponible para lectores.
    """
    form = PrestamoForm()
    form.libro_id.choices = [(libro.id, libro.titulo)
                             for libro in Libro.query.filter_by(disponible=True).all()]

    if form.validate_on_submit():
        prestamo = Prestamo(
            usuario_id=current_user.id,
            libro_id=form.libro_id.data,
            fecha_prestamo=form.fecha_prestamo.data,
            fecha_devolucion=form.fecha_devolucion.data
        )
        libro = Libro.query.get(form.libro_id.data)
        libro.disponible = False  # Marca el libro como no disponible
        db.session.add(prestamo)
        db.session.commit()
        flash("Préstamo registrado exitosamente.")
        return redirect(url_for('main.dashboard'))

    return render_template('prestamo_form.html', form=form)


@main.route('/usuarios')
@login_required
def listar_usuarios():
    if current_user.role.name != 'Admin':
        flash("No tienes permiso para ver esta página.")
        return redirect(url_for('main.dashboard'))

    # Obtener instancias completas de usuarios con sus roles (no usar .add_columns)
    usuarios = User.query.join(User.role).all()

    return render_template('usuarios.html', usuarios=usuarios)


@main.route('/libros/listar')
@login_required
def listar_libros():
    """
    Permite listar los libros disponibles.
    """
    if current_user.role.name == 'Lector':
        libros = Libro.query.filter_by(disponible=True).all()
    else:
        libros = Libro.query.all()  # Admin y bibliotecarios pueden ver todos los libros

    return render_template('libros.html', libros=libros)
