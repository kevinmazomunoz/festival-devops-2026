CREATE DATABASE IF NOT EXISTS festival;

USE festival;

CREATE TABLE IF NOT EXISTS artistas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO artistas (nombre) VALUES
('DJ Docker'),
('Flask Beats'),
('Kubernetes Live');