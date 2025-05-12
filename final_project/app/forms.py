from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Formulario para login de usuario
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Formulario para registrar un nuevo usuario
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
   
    role = SelectField(
        'Role',
        choices=[('Lector', 'Lector'), ('Bibliotecario', 'Bibliotecario'), ('Admin', 'Admin')],
        validators=[DataRequired()]
    )

    submit = SubmitField('Register')

# Formulario para cambiar la contraseña del usuario
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm new password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Update Password')

# Formulario para crear o editar un libro
class LibroForm(FlaskForm):
    titulo = StringField('Book title', validators=[DataRequired()])
    descripcion = TextAreaField('Description', validators=[DataRequired()])
    autor = StringField('Author', validators=[DataRequired()])
    submit = SubmitField('Save')

# Formulario para registrar un préstamo de libro
class PrestamoForm(FlaskForm):
    libro_id = SelectField('Book', coerce=int, validators=[DataRequired()])
    fecha_prestamo = DateField('Loan Date', format='%Y-%m-%d', validators=[DataRequired()])
    fecha_devolucion = DateField('Return Date', format='%Y-%m-%d')
    submit = SubmitField('Register Loan')
