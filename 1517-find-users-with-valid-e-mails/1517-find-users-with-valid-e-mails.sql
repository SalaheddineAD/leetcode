# Write your MySQL query statement below
SELECT * 
FROM users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\\?com)?\\.com$'