from flask import Blueprint, request, jsonify
from app.models import db, Libro, Role
from flask_login import current_user, login_required

# Blueprint para libros
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/dashboard')
def index():
    """
    Página de inicio pública (home).
    """
    return '<h1>Corriendo el Gestor de Biblioteca.</h1>'

# Lista todos los libros
@main.route('/libros', methods=['GET'])
def listar_libros():
    """
    Retorna una lista de libros (JSON).
    """
    libros = Libro.query.all()

    data = [
        {'id': libro.id, 'titulo': libro.titulo, 'autor': libro.autor, 'descripcion': libro.descripcion}
        for libro in libros
    ]
    return jsonify(data), 200

# Lista un solo libro por su ID
@main.route('/libros/<int:id>', methods=['GET'])
def listar_un_libro(id):
    """
    Retorna un solo libro por su ID (JSON).
    """
    libro = Libro.query.get_or_404(id)

    data = {
        'id': libro.id,
        'titulo': libro.titulo,
        'autor': libro.autor,
        'descripcion': libro.descripcion
    }

    return jsonify(data), 200

# Solo Bibliotecarios o Admin pueden crear un libro
@main.route('/libros', methods=['POST'])
@login_required
def crear_libro():
    """
    Crea un libro solo si el usuario tiene el rol adecuado (Bibliotecario o Admin).
    """
    if current_user.role.name not in ['Bibliotecario', 'Admin']:
        return jsonify({'error': 'No tienes permisos para agregar libros'}), 403

    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    libro = Libro(
        titulo=data.get('titulo'),
        autor=data.get('autor'),
        descripcion=data.get('descripcion')
    )

    db.session.add(libro)
    db.session.commit()

    return jsonify({'message': 'Libro creado', 'id': libro.id}), 201

# Solo Bibliotecarios o Admin pueden actualizar un libro
@main.route('/libros/<int:id>', methods=['PUT'])
@login_required
def actualizar_libro(id):
    """
    Actualiza un libro solo si el usuario tiene el rol adecuado (Bibliotecario o Admin).
    """
    if current_user.role.name not in ['Bibliotecario', 'Admin']:
        return jsonify({'error': 'No tienes permisos para actualizar libros'}), 403

    libro = Libro.query.get_or_404(id)
    data = request.get_json()

    libro.titulo = data.get('titulo', libro.titulo)
    libro.autor = data.get('autor', libro.autor)
    libro.descripcion = data.get('descripcion', libro.descripcion)

    db.session.commit()

    return jsonify({'message': 'Libro actualizado', 'id': libro.id}), 200

# Solo Bibliotecarios o Admin pueden eliminar un libro
@main.route('/libros/<int:id>', methods=['DELETE'])
@login_required
def eliminar_libro(id):
    """
    Elimina un libro solo si el usuario tiene el rol adecuado (Bibliotecario o Admin).
    """
    if current_user.role.name not in ['Bibliotecario', 'Admin']:
        return jsonify({'error': 'No tienes permisos para eliminar libros'}), 403

    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()

    return jsonify({'message': 'Libro eliminado', 'id': libro.id}), 200
