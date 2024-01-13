WITH tmp AS (
    SELECT reports_to, COUNT(*) AS reports_count, ROUND(AVG(age)) AS average_age
    FROM employees
    GROUP BY reports_to
)
SELECT employee_id, name, reports_count, average_age
FROM employees e JOIN tmp t
ON t.reports_to = e.employee_id
ORDER BY employee_id