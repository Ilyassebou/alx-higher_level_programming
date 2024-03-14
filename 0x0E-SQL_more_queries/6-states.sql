-- Check if the database exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Check if the table exists and create it if it doesn't
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
