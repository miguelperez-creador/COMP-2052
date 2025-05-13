from app import create_app, db
from app.models import Role, User
from werkzeug.security import generate_password_hash  # Por si necesitas usarlo directamente

# Crear la aplicación Flask
app = create_app()

# Contexto de aplicación necesario para operaciones con la base de datos
with app.app_context():
    # Asegurarse de que los roles existen
    roles = ['Admin', 'Bibliotecario', 'Lector']
    for role_name in roles:
        if not Role.query.filter_by(name=role_name).first():
            new_role = Role(name=role_name)
            db.session.add(new_role)
            print(f'✅ Rol "{role_name}" creado.')

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
            "username": "John Doe",
            "email": "bibliotecario@example.com",
            "password": "bibliotecario123",
            "role_name": "Bibliotecario"
        },
        {
            "username": "Steve Jobs",
            "email": "lector@example.com",
            "password": "lector123",
            "role_name": "Lector"
        }
    ]

    for user_info in users_data:
        if not User.query.filter_by(email=user_info['email']).first():
            role = Role.query.filter_by(name=user_info['role_name']).first()
            user = User(
                username=user_info['username'],
                email=user_info['email'],
                role=role
            )
            user.set_password(user_info['password'])  # Genera hash seguro
            db.session.add(user)
            print(f'✅ Usuario "{user.username}" creado con rol "{role.name}".')
        else:
            print(f'ℹ️ El usuario con email {user_info["email"]} ya existe.')

    db.session.commit()
    print("✅ Todos los usuarios fueron procesados correctamente.")
