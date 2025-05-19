from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Carga un usuario desde su ID (para sesiones)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Modelo de roles (Admin, Bibliotecario, Lector, etc.)


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)

    users = db.relationship('User', backref='role', lazy=True)

# Modelo de usuario


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    prestamos = db.relationship('Prestamo', backref='usuario', lazy=True)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

# Modelo de autor


class Autor(db.Model):
    __tablename__ = 'autor'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    libros = db.relationship('Libro', backref='autor', lazy=True)

# Modelo de libro


class Libro(db.Model):
    __tablename__ = 'libro'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'), nullable=False)
    disponible = db.Column(db.Boolean, default=True)
    isbn = db.Column(db.String(13))
    prestamos = db.relationship('Prestamo', backref='libro', lazy=True)

# Modelo de préstamo de libros


class Prestamo(db.Model):
    __tablename__ = 'prestamo'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    libro_id = db.Column(db.Integer, db.ForeignKey('libro.id'), nullable=False)
    fecha_prestamo = db.Column(db.Date, nullable=False)
    fecha_devolucion = db.Column(db.Date, nullable=True)
