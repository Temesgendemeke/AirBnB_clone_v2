-- Prepares the MySQL server for this project test 
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
SET GLOBAL validate_password.policy=LOW;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
SET GLOBAL validate_password.policy=MEDIUM;
FLUSH PRIVILEGES;