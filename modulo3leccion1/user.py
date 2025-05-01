from flask_login import UserMixin

# Usuarios simulados en memoria
usuarios = {
    'juan': {'id': '1', 'username': 'juan', 'password': '1234'},
    'maria': {'id': '2', 'username': 'maria', 'password': 'abcd'}
}

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

def get_user_by_id(user_id):
    # Devuelve el usuario con el id proporcionado
    for user in usuarios.values():
        if user['id'] == user_id:
            return User(user['id'], user['username'], user['password'])
    return None

def get_user_by_username(username):
    # Devuelve el usuario con el nombre de usuario proporcionado
    user = usuarios.get(username)
    if user:
        return User(user['id'], user['username'], user['password'])
    return None

def validate_user(username, password):
    
    user = usuarios.get(username)
    return user and user['password'] == password
