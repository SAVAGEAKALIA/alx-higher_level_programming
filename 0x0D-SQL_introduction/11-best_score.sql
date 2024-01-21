-- Script to Search Table from Database
-- Based on score greater or equal to 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

