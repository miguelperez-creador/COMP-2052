from flask import Blueprint, request, jsonify
from app.models import db, Libro

# Blueprint solo con endpoints de prueba para libros
main = Blueprint('main', __name__)

@main.route('/')  # Ambas rutas llevan al mismo lugar
@main.route('/dashboard')
def index():
    """
    Página de inicio pública (home).
    """
    return '<h1>Corriendo en Modo de Prueba para la Biblioteca.</h1>'

@main.route('/libros', methods=['GET'])
def listar_libros():
    """
    Retorna una lista de libros (JSON).
    """
    libros = Libro.query.all()

    data = [
        {'id': libro.id, 'titulo': libro.titulo, 'descripcion': libro.descripcion, 'autor': libro.autor, 'disponible': libro.disponible}
        for libro in libros
    ]
    return jsonify(data), 200


@main.route('/libros/<int:id>', methods=['GET'])
def listar_un_libro(id):
    """
    Retorna un solo libro por su ID (JSON).
    """
    libro = Libro.query.get_or_404(id)

    data = {
        'id': libro.id,
        'titulo': libro.titulo,
        'descripcion': libro.descripcion,
        'autor': libro.autor,
        'disponible': libro.disponible
    }

    return jsonify(data), 200


@main.route('/libros', methods=['POST'])
def crear_libro():
    """
    Crea un libro sin validación.
    Espera JSON con 'titulo', 'descripcion', 'autor' y 'disponible'.
    """
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    libro = Libro(
        titulo=data.get('titulo'),
        descripcion=data.get('descripcion'),
        autor=data.get('autor'),
        disponible=data.get('disponible', True)  # Default a True si no se proporciona
    )

    db.session.add(libro)
    db.session.commit()

    return jsonify({'message': 'Libro creado', 'id': libro.id, 'titulo': libro.titulo}), 201

@main.route('/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    """
    Actualiza un libro sin validación de permisos.
    """
    libro = Libro.query.get_or_404(id)
    data = request.get_json()

    libro.titulo = data.get('titulo', libro.titulo)
    libro.descripcion = data.get('descripcion', libro.descripcion)
    libro.autor = data.get('autor', libro.autor)
    libro.disponible = data.get('disponible', libro.disponible)

    db.session.commit()

    return jsonify({'message': 'Libro actualizado', 'id': libro.id}), 200

@main.route('/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    """
    Elimina un libro sin validación de permisos.
    """
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()

    return jsonify({'message': 'Libro eliminado', 'id': libro.id}), 200