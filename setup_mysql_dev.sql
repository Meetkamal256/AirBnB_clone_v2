-- script that prepares a MySQL server for the project
-- creates database and user
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'  IDENTIFIED BY 'Kamal256$';
 GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
 GRANT SELECT ON performance_schema.* to 'hbnb_dev'@'localhost';