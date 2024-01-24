-- script that lists all the cities in database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

