# Write your MySQL query statement below
SELECT employee_id 
FROM employees
WHERE salary< 30000 AND manager_id NOT IN (
    SELECT employee_id from employees
)
ORDER BY employee_id