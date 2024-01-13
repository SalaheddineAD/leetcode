# Write your MySQL query statement below
WITH tmp AS (SELECT name, salary, departmentId, DENSE_RANK() OVER( PARTITION BY departmentId ORDER BY salary DESC) salary_rank
FROM employee
)
SELECT department.name as Department, tmp.name as Employee, salary
FROM tmp INNER JOIN department
ON tmp.departmentID = department.id
WHERE salary_rank<=3
