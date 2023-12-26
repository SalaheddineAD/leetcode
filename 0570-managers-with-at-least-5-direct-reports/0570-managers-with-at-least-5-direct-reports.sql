WITH managers as(
    SELECT managerId, count(managerId) as countManagers
    FROM employee
    GROUP BY managerId
)  
SELECT name 
FROM employee
WHERE id IN (
SELECT managerId
FROM managers
WHERE countManagers>=5
)