-- Create the snakegame database if it doesn't exists
CREATE DATABASE snakegame_db;

-- Connect to the snakegame database
\c snakegame_db;

-- Create the scores table if it doesn't exist
CREATE TABLE Score (
    userID INTEGER PRIMARY KEY,
    userName VARCHAR(25),
    score INTEGER NOT NULL,
    date TIMESTAMP
);
