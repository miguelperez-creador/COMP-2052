
-- Eliminar la base de datos si existe
DROP DATABASE IF EXISTS gestor_biblioteca;

-- Crear y usar la base de datos
CREATE DATABASE gestor_biblioteca
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE gestor_biblioteca;

-- Crear tabla de roles
CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64) UNIQUE NOT NULL
);

-- Crear tabla de usuarios
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    role_id INT,
    FOREIGN KEY (role_id) REFERENCES role(id)
);

-- Crear tabla de autores
CREATE TABLE autor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Crear tabla de libros
CREATE TABLE libro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    autor_id INT NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    categoria VARCHAR(50),
    estado ENUM('Disponible', 'Prestado') DEFAULT 'Disponible',
    anio_publicacion INT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descripcion TEXT,
    FOREIGN KEY (autor_id) REFERENCES autor(id)
);

-- Insertar los roles iniciales
INSERT INTO role (name) VALUES ('Admin'), ('Bibliotecario'), ('Lector');
