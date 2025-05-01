from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # Cambia esta clave por una más segura

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Simulación de base de datos de usuarios (esto debería ser una base de datos real)
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Diccionario de usuarios de ejemplo (en un caso real, los usuarios deben ser almacenados en una base de datos)
users = {'usuario1': {'password': 'contraseña1'}, 'usuario2': {'password': 'contraseña2'}}

# Cargar usuario
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        
        if user and user['password'] == password:
            user_obj = User(username)
            login_user(user_obj)
            return redirect(url_for('dashboard'))
        else:
            return 'Credenciales inválidas', 401

    return render_template('login.html')

@app.route('/dashboard')
@login_required  # Ruta protegida, solo accesible si el usuario está autenticado
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
