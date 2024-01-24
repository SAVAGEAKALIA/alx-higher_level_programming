-- script that creates user_0d_1
-- grants user_0d_1 all priveledges
-- sets password
-- should fail if user_0d_1 exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
