-- Script that computes the same score for all records in the table second_table
-- The number of records for this score with the label number
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
