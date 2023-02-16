-- List all cities in db 'hbtn_0d_usa'
-- Joins voth tables on state_id and foreign key cities.state_id
-- Each record displays cities.id, cities.name, and states.name
-- Can only use SELECT statement once
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
