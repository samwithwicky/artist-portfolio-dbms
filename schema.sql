CREATE DATABASE IF NOT EXISTS artist_portfolio_db;
USE artist_portfolio_db;

CREATE TABLE artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    bio TEXT
);

CREATE TABLE portfolio (
    portfolio_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    artist_id INT NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
        ON DELETE CASCADE
);

CREATE TABLE artwork (
    artwork_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    medium VARCHAR(50),
    year_created INT CHECK (year_created >= 1900),
    image_path VARCHAR(255),
    portfolio_id INT NOT NULL,
    FOREIGN KEY (portfolio_id) REFERENCES portfolio(portfolio_id)
        ON DELETE CASCADE
);

CREATE TABLE category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE artwork_category (
    artwork_id INT,
    category_id INT,
    PRIMARY KEY (artwork_id, category_id),
    FOREIGN KEY (artwork_id) REFERENCES artwork(artwork_id)
        ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
        ON DELETE CASCADE
);

-- SOURCE D:/projects/artwork/schema.sql;