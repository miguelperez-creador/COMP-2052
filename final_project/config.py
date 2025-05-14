import os


class Config:
    """
    Configuración general para la aplicación Gestor de Biblioteca.
    Esta clase puede extenderse para diferentes entornos
    como desarrollo, producción o pruebas.
    """

    # Clave secreta para sesiones y protección CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta-flask')

    # URI de conexión a la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://root:root@localhost/gestor_biblioteca'
    )

    # Desactiva el seguimiento de modificaciones de objetos (mejora el rendimiento)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Protección CSRF habilitada
    CSRF_ENABLED = True

    # Definición de roles disponibles en el sistema
    ROLES = {
        'lector': 'Lector',
        'bibliotecario': 'Bibliotecario',
        'admin': 'Admin'
    }

    # Configuraciones para Flask-Login
    REMEMBER_COOKIE_DURATION = 3600 * 24 * 7  # Duración de la cookie "recordarme" (7 días)
    SESSION_PERMANENT = False                # Las sesiones no son permanentes por defecto
    SESSION_TYPE = "filesystem"              # Tipo de almacenamiento de sesiones (útil para Flask-Session)
    LOGIN_VIEW = 'auth.login'                # Ruta del login (puedes cambiarla según tu blueprint)
    LOGIN_MESSAGE = "Por favor, inicia sesión para acceder a esta página."
