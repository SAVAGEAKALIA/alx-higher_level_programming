-- STILL Temperature sort
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)  -- Filter for July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;  -- Retrieve only the top 3 results
