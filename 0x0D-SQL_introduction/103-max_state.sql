-- displays the max temperature of each state (ordered by State name).
SELECT state, MAX(value) GROUP BY state 
ORDER BY state;