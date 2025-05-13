import os


class Config:
    """
    Configuración general para la aplicación Gestor de Biblioteca.
    Esta clase puede extenderse para diferentes entornos 
    como desarrollo, producción o pruebas.
    """

    # Clave secreta para sesiones y protección CSRF
    # En producción, se recomienda definir esta variable en las variables de entorno
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

    # Puedes añadir aquí otras configuraciones necesarias, como paginación, logs, etc.
