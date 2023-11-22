-- Script preparing MySQL server for the project
-- Creation of a developement database called hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creation of a  new user called hbnb_dev and will have all privileges on the database
-- Allocated password : hbnb_dev_pwd if it dosen't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Command to grant all privileges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-- Giving only SELECT privilege for the user hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
