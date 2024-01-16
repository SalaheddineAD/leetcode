# Write your MySQL query statement below

# SELECT category, COUNT(*) AS accounts_count
# FROM(
#     SELECT category, COUNT(*) AS accounts_count
#     FROM (
#         SELECT CASE
#         WHEN income< 20000 THEN "Low Salary"
#         WHEN income> 50000 THEN "High Salary"
#         WHEN income>=20000 AND income<=50000 THEN "Average Salary"
#         END AS category
#         FROM accounts) AS s
#     GROUP BY category) AS q
# WHERE accounts_count>0
SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count 
FROM Accounts 
WHERE income < 20000
UNION
SELECT 'Average Salary' AS category, COUNT(*) AS accounts_count 
FROM Accounts 
WHERE income BETWEEN 20000 AND 50000
UNION
SELECT 'High Salary' AS category, COUNT(*) AS accounts_count 
FROM Accounts 
WHERE income > 50000;