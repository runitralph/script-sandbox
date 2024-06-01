CREATE DATABASE protein_db;
USE protein_db;

CREATE TABLE proteins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sequence TEXT NOT NULL,
    description TEXT
);
