SELECT name 
FROM employee
WHERE id IN (
SELECT managerId
FROM employee
    GROUP BY managerId 
    HAVING COUNT(*) >= 5
)