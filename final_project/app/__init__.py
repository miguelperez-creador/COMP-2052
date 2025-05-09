from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    # Registra primero autenticación para proteger rutas desde el inicio
    from app.auth_routes import auth
    app.register_blueprint(auth)

    # Registra las rutas principales (por ejemplo, gestión de libros)
    from app.routes import main  # Considera renombrarlo a books si es solo para libros
    app.register_blueprint(main)

    return app
