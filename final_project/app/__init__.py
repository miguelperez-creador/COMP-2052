from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

# Inicializar extensiones sin app por ahora
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Redirige a esta ruta si no hay sesión

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones con la app
    db.init_app(app)
    login_manager.init_app(app)
    Migrate(app, db)

    # Registrar blueprints
    from app.auth_routes import auth
    app.register_blueprint(auth)

    from app.routes import main
    app.register_blueprint(main)

    return app
