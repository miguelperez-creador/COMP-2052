from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Formulario para login de usuario
class LoginForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

# Formulario para registrar un nuevo usuario
class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('password')])
    
    role = SelectField(
        'Rol',
        choices=[('Lector', 'Lector'), ('Bibliotecario', 'Bibliotecario'), ('Admin', 'Admin')],
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
class LibroForm(FlaskForm):
    titulo = StringField('Título del libro', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    autor = StringField('Autor', validators=[DataRequired()])
    categoria_id = SelectField('Categoría', coerce=int, validators=[DataRequired()])
    disponible = SelectField(
        'Disponible',
        choices=[(True, 'Sí'), (False, 'No')],
        coerce=lambda x: x == 'True',
        validators=[DataRequired()]
    )
    submit = SubmitField('Guardar')

# Formulario para registrar un préstamo de libro
class PrestamoForm(FlaskForm):
    libro_id = SelectField('Libro', coerce=int, validators=[DataRequired()])
    fecha_prestamo = DateField('Fecha de préstamo', format='%Y-%m-%d', validators=[DataRequired()])
    fecha_devolucion = DateField('Fecha de devolución', format='%Y-%m-%d')
    submit = SubmitField('Registrar préstamo')
