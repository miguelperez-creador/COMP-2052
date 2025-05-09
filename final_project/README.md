# 📚 Gestor de Biblioteca - Flask + MySQL

Este proyecto permite gestionar una biblioteca donde los **bibliotecarios** pueden añadir libros, los **lectores** pueden visualizarlos, y los **administradores** pueden gestionar usuarios y roles. Es el Proyecto 2 dentro de una colección de 11 proyectos desarrollados como práctica final para los estudiantes.

A continuación, capturas de algunas de la interfaces del front-end del proyecto:

<figure class="image">
   <img src="images/image-01.png" alt="Login Form">
   <figcaption>Página de Inicio de Sesión</figcaption>
</figure>

<figure class="image">
   <img src="images/image-02.png" alt="Dashboard">
   <figcaption>Panel Principal / Dashboard</figcaption>
</figure>

<figure class="image">
   <img src="images/image-03.png" alt="User List">
   <figcaption>Usuarios Registrados</figcaption>
</figure>

## 🚀 Tecnologías utilizadas

- **Flask** – Framework backend en Python  
- **Flask-Login** – Sistema de autenticación  
- **MySQL** – Base de datos relacional  
- **SQLAlchemy** – ORM para la base de datos  
- **Bootstrap 5** – Framework CSS responsivo  
- **Jinja2** – Motor de plantillas para HTML  

---

## 📂 Estructura del proyecto

| Archivo / Carpeta        | Descripción                                                             |
|--------------------------|-------------------------------------------------------------------------|
| `create_demo_users.py`   | Script para crear usuarios iniciales con roles y contraseñas            |
| `config.py`              | Configuración de Flask (DB URI, claves, etc.)                           |
| `README.md`              | Este archivo de documentación del proyecto                              |
| `requirements.txt`       | Lista de paquetes Python requeridos                                     |
| `run.py`                 | Punto de entrada para ejecutar el servidor Flask                        |
| `app/__init__.py`        | Inicializa la aplicación Flask                                          |
| `app/models.py`          | Contiene los modelos SQLAlchemy: User, Role, Libro                      |
| `app/forms.py`           | Formularios usados en login, registro, libros, contraseñas              |
| `app/routes.py`          | Rutas principales del proyecto (dashboard, libros, cambiar contraseña)  |
| `app/auth_routes.py`     | Rutas para autenticación (login, registro, logout)                      |
| `app/templates/*.html`   | Plantillas HTML para las vistas principales                             |
| `static/css/styles.css`  | Archivo CSS personalizado (opcional)                                    |
| `database_schema/02_biblioteca.sql` | SQL para crear la base de datos de la biblioteca       |

---

## 📚 Proyectos Finales Asignables

| Nº | Proyecto             | CRUD Principal | Roles                        |
|----|----------------------|----------------|------------------------------|
| 2  | Gestor de Biblioteca | Libros         | Lector, Bibliotecario, Admin |

---

## 🧪 Requisitos previos

- Python 3.8 o superior  
- MySQL Server corriendo localmente (`localhost:3306`)  
- Un entorno virtual activo (opcional)  

---

## ⚙️ Instalación del proyecto

1. **Clonar el repositorio**

```bash
git clone https://github.com/turepositorio/grupo-biblioteca.git
cd grupo-biblioteca
