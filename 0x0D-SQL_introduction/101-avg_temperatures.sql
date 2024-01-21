-- sorting temperature dump file
SELECT city, AVG(temp) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
