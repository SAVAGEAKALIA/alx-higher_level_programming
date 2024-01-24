-- Once again temp sorting by city
SELECT state, MAX(temp) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY max_temp DESC;
