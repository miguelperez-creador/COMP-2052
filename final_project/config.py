import os


class Config:
    """
    Configuración general para la aplicación Gestor de Biblioteca.
    Esta clase puede extenderse para diferentes entornos (desarrollo, producción, pruebas, etc.).
    """

    # Clave secreta para sesiones y protección CSRF
    # ⚠️ En producción, se recomienda definir esta variable en el entorno
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-secreta-flask')

    # URI de conexión a la base de datos
    # Puedes usar otra según tu gestor (PostgreSQL, SQLite, etc.)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
<<<<<<< HEAD
        'mysql+pymysql://root:root@localhost/gestion_biblioteca'
=======
        'mysql+pymysql://root:root@localhost/gestion_biblioteca'  # Modificado para biblioteca
>>>>>>> 1703a668491d341c2c7aab5aa1cd229b83895dbb
    )

    # Desactiva el seguimiento de modificaciones para mejorar el rendimiento
    SQLALCHEMY_TRACK_MODIFICATIONS = False

<<<<<<< HEAD
    # Protección CSRF habilitada
    CSRF_ENABLED = True

    # Definición de roles disponibles en el sistema
=======
    # Configuración para roles en el sistema
    # Esta es solo una sugerencia, puedes adaptarlo según lo que necesites
>>>>>>> 1703a668491d341c2c7aab5aa1cd229b83895dbb
    ROLES = {
        'lector': 'Lector',
        'bibliotecario': 'Bibliotecario',
        'admin': 'Admin'
    }

<<<<<<< HEAD
    # Puedes añadir aquí otras configuraciones necesarias, como paginación, logs, etc.
=======
    # Configuración adicional para validaciones de seguridad
    # Puedes agregar más reglas aquí si es necesario, como CSRF, etc.
    CSRF_ENABLED = True  # Habilitar protección CSRF
>>>>>>> 1703a668491d341c2c7aab5aa1cd229b83895dbb
