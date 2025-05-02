from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import BookForm
from app.models import db, User, Role, Book
from flask_login import login_required, current_user

# Blueprint principal para la gestión de libros
main = Blueprint('main', __name__)

@main.route('/dashboard')
@login_required
def dashboard():
    """
    Página principal para el Lector: solo lectura de libros.
    """
    books = Book.query.all()  # Trae todos los libros
    return render_template('dashboard.html', books=books)

@main.route('/admin_dashboard')
@login_required
def admin_dashboard():
    """
    Página para el Admin: vista de administración general.
    Solo puede ser accesible por usuarios con rol "Admin".
    """
    if current_user.role.name != 'Admin':
        return redirect(url_for('main.dashboard'))
    
    # Lógica adicional si el usuario es Admin
    return render_template('admin_dashboard.html')

@main.route('/librarian_dashboard')
@login_required
def librarian_dashboard():
    """
    Página para el Bibliotecario: gestión de libros.
    Solo puede ser accesible por "Bibliotecario" o "Admin".
    """
    if current_user.role.name not in ['Bibliotecario', 'Admin']:
        return redirect(url_for('main.dashboard'))
    
    books = Book.query.all()
    return render_template('librarian_dashboard.html', books=books)

@main.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    """
    Permite a Bibliotecarios y Admin agregar nuevos libros.
    """
    if current_user.role.name not in ['Bibliotecario', 'Admin']:
        flash('No tienes permisos para agregar libros.')
        return redirect(url_for('main.dashboard'))
    
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            autor=form.autor.data
        )
        db.session.add(book)
        db.session.commit()
        flash('Libro agregado exitosamente.')
        return redirect(url_for('main.librarian_dashboard'))

    return render_template('add_book.html', form=form)

@main.route('/edit_book/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_book(id):
    """
    Permite a Bibliotecarios y Admin editar detalles de un libro.
    """
    if current_user.role.name not in ['Bibliotecario', 'Admin']:
        flash('No tienes permisos para editar libros.')
        return redirect(url_for('main.dashboard'))
    
    book = Book.query.get_or_404(id)
    form = BookForm(obj=book)
    
    if form.validate_on_submit():
        book.titulo = form.titulo.data
        book.descripcion = form.descripcion.data
        book.autor = form.autor.data
        db.session.commit()
        flash('Libro editado exitosamente.')
        return redirect(url_for('main.librarian_dashboard'))
    
    return render_template('edit_book.html', form=form, book=book)

@main.route('/delete_book/<int:id>', methods=['POST'])
@login_required
def delete_book(id):
    """
    Permite a Bibliotecarios y Admin eliminar un libro.
    """
    if current_user.role.name not in ['Bibliotecario', 'Admin']:
        flash('No tienes permisos para eliminar libros.')
        return redirect(url_for('main.dashboard'))

    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('Libro eliminado exitosamente.')
    return redirect(url_for('main.librarian_dashboard'))
