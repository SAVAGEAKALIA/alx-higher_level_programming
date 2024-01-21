-- Script that computes the score average of all records in the table second_table
-- The result column name should be average
USE hbtn_0c_0
ALTER TABLE second_table ADD average DECIMAL(4, 4);

SELECT AVG(SCORE) AS average
FROM second_table


