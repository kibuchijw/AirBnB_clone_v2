-- A script that prepares a MySQL server for the project 
-- Creating a test database with name hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creating a new user called hbnb_test on the database
-- Setting the password  of the new user to hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Assigning only select priviledge to the new user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILeGES;

-- Granting all prviledges to the new user on hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
