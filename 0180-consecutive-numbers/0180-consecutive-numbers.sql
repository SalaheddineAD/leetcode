# Write your MySQL query statement below
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM logs l1 inner join logs l2
ON l1.id = l2.id-1
INNER JOIN logs l3
ON l2.id = L3.id-1
WHERE l1.num = l2.num AND l2.num = l3.num