-- Eliminar la base de datos si existe
DROP DATABASE IF EXISTS gestor_biblioteca;

-- Usar la base de datos recién creada
DROP DATABASE IF EXISTS gestor_biblioteca;
CREATE DATABASE gestor_biblioteca
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE gestor_biblioteca;

-- Crear la tabla de roles
CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64) UNIQUE NOT NULL
);

-- Crear la tabla de usuarios
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    role_id INT,
    FOREIGN KEY (role_id) REFERENCES role(id)
);

-- Crear la tabla de libros
CREATE TABLE libro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    categoria VARCHAR(50),
    estado ENUM('Disponible', 'Prestado') DEFAULT 'Disponible',
    anio_publicacion INT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    ALTER TABLE libro ADD COLUMN descripcion TEXT;
);

-- Insertar los roles iniciales
INSERT INTO role (name) VALUES ('Admin'), ('Bibliotecario'), ('Lector');
