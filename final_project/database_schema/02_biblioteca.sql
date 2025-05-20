<<<<<<< HEAD
=======
-- Active: 1747575679602@@127.0.0.1@3306@gestor_biblioteca
>>>>>>> 486c39d8256263668fb62fccea47db337a8c5966
DROP DATABASE IF EXISTS gestor_biblioteca;
CREATE DATABASE gestor_biblioteca
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE gestor_biblioteca;

-- Tabla de roles
CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64) UNIQUE NOT NULL
);

-- Tabla de usuarios
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(256) NOT NULL,
    role_id INT,
    FOREIGN KEY (role_id) REFERENCES role(id)
);

-- Tabla de autores
CREATE TABLE autor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de libros con relación a autor
CREATE TABLE libro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    descripcion TEXT,
    autor_id INT,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    categoria VARCHAR(50),
    disponible BOOLEAN DEFAULT TRUE,
    anio_publicacion INT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (autor_id) REFERENCES autor(id)
);

-- Insertar roles
INSERT INTO role (name) VALUES ('Admin'), ('Bibliotecario'), ('Lector');
