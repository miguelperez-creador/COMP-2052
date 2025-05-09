from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Formulario para login de usuario
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

# Formulario para registrar un nuevo usuario
class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('password')])
    
    role = SelectField(
        'Rol',
        choices=[
            ('Lector', 'Lector'),
            ('Bibliotecario', 'Bibliotecario'),
            ('Admin', 'Admin')
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField('Registrar')

# Formulario para cambiar la contraseña del usuario
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Contraseña actual', validators=[DataRequired()])
    new_password = PasswordField('Nueva contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar nueva contraseña', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Actualizar contraseña')

# Formulario para crear o editar un libro
class BookForm(FlaskForm):
    titulo = StringField('Título del libro', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    autor = StringField('Autor', validators=[DataRequired()])
    submit = SubmitField('Guardar')
