--  lists all records of the table second_table name and score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;