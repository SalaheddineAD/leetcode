# Write your MySQL query statement below
SELECT s1.id, COALESCE(if (s1.id%2!=0,(
    SELECT student FROM seat s2 WHERE s2.id=s1.id+1
    ),(
    SELECT student FROM seat s2 WHERE s2.id=s1.id-1
    )),s1.student) AS student
FROM seat s1 
