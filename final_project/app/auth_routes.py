from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import LoginForm, RegisterForm
from app.models import db, User, Role
from flask_login import login_user, logout_user

# Blueprint de autenticación: gestiona login, registro y logout
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Inicia sesión de un usuario existente si las credenciales son válidas.
    """
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)

            # Redirige según el rol (opcional)
            if user.role.name == "Admin":
                return redirect(url_for('main.admin_dashboard'))
            elif user.role.name == "Bibliotecario":
                return redirect(url_for('main.librarian_dashboard'))
            else:
                return redirect(url_for('main.dashboard'))

        flash('Credenciales inválidas.')

    return render_template('login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Registra un nuevo usuario y lo asocia por defecto al rol seleccionado.
    """    
    form = RegisterForm()
    
    if form.validate_on_submit():
        role = Role.query.filter_by(name=form.role.data).first()

        
        if not role:
            role = Role(name=form.role.data)
            db.session.add(role)
            db.session.commit()

        user = User(
            username=form.username.data,
            email=form.email.data,
            role=role
        )
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Usuario registrado con éxito.')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    """
    Cierra sesión del usuario actual y redirige al login.
    """
    logout_user()
    return redirect(url_for('auth.login'))
