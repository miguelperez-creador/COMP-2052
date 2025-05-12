from app import create_app, db
from app.models import Role, User
from werkzeug.security import generate_password_hash  # Por si necesitas usarlo directamente

# Crear la aplicación Flask
app = create_app()

# Contexto de aplicación necesario para operaciones con la base de datos
with app.app_context():
    # Crear roles si no existen
    roles = ['Admin', 'Bibliotecario', 'Lector']
    for role_name in roles:
        if not Role.query.filter_by(name=role_name).first():
            new_role = Role(name=role_name)
            db.session.add(new_role)
            print(f'Rol "{role_name}" creado.')

    db.session.commit()

    # Datos de usuarios iniciales
    users_data = [
        {
            "username": "Administrator",
            "email": "admin@example.com",
            "password": "admin123",
            "role_name": "Admin"
        },
        {
            "username": "Bibliotecario Uno",
            "email": "librarian@example.com",
            "password": "librarian123",
            "role_name": "Bibliotecario"
        },
        {
            "username": "Juan Pérez",
            "email": "lector@example.com",
            "password": "lector123",
            "role_name": "Lector"
        }
    ]

    # Crear usuarios si no existen
    for user_info in users_data:
        if not User.query.filter_by(email=user_info['email']).first():
            role = Role.query.filter_by(name=user_info['role_name']).first()
            if role:
                user = User(
                    username=user_info['username'],
                    email=user_info['email'],
                    role=role
                )
                user.set_password(user_info['password'])  # Método seguro para hashear contraseña
                db.session.add(user)
                print(f'Usuario "{user.username}" creado con rol "{role.name}".')
            else:
                print(f'Rol "{user_info["role_name"]}" no encontrado. No se creó el usuario.')
        else:
            print(f'El usuario con email "{user_info["email"]}" ya existe.')

    db.session.commit()
    print("Todos los usuarios fueron procesados correctamente.")
