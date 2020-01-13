--DROP DATABASE kapperapp;
--DROP USER 'kapper'@'localhost';

CREATE DATABASE kapperapp;
USE kapperapp;

CREATE USER 'kapper'@'localhost' IDENTIFIED BY 'k@pp3r';
GRANT ALL PRIVILEGES ON * . * TO 'kapper'@'localhost';

CREATE TABLE afspraak
(
    id INTEGER PRIMARY KEY NOT NULL
    AUTO_INCREMENT,
    naam VARCHAR
    (256) NOT NULL,
    email VARCHAR
    (256) NOT NULL,
    tijdstip DATETIME NOT NULL
);