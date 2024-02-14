-- script that lists all the cities of california that can be found in the database hbtn_0d_usa.

SELECT id, name from cities
UNION
SELECT id, name FROM states
WHERE name == "California"
ORDER BY cities.id;
