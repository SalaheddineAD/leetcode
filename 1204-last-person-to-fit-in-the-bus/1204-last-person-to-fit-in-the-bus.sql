# Write your MySQL query statement below
SELECT  person_name
FROM (SELECT *, SUM(weight) OVER( ORDER BY turn) as cumulativeSum
FROM queue) AS S
WHERE cumulativeSum<=1000
ORDER BY cumulativeSum DESC
LIMIT 1;