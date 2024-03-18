-- Create the snakegame database if it doesn't exists
CREATE DATABASE snakegame_db;

-- Connect to the snakegame database
\c snakegame_db;

-- Create the scores table if it doesn't exist
CREATE TABLE score (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(25),
    score INTEGER NOT NULL,
    date TIMESTAMP
);
