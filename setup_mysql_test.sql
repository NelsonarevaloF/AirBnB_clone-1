-- this script create a DB with the Specifications of holberton
-- we are going to create DB to storage the objects of the console
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
