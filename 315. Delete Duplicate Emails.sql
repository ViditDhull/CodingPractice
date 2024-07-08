WITH CTE AS (
    SELECT MIN(id) as id
    FROM person
    GROUP BY email
)
DELETE
FROM Person
WHERE id NOT IN (SELECT id FROM CTE);
