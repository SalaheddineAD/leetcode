# Write your MySQL query statement below
WITH root AS (
    SELECT id
    FROM tree
    WHERE p_id IS NULL
)

SELECT id, CASE 
            WHEN id in (SELECT id FROM root) THEN "Root"
            WHEN id in (SELECT p_id FROM tree) THEN "Inner"
            ELSE "Leaf"
            END AS type
FROM tree