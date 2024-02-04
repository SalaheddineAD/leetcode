SELECT visited_on,
amount + amount1 + amount2 + amount3 + amount4 + amount5 + amount6 AS amount,
ROUND((amount + amount1 + amount2 + amount3 + amount4 + amount5 + amount6)/7,2) AS average_amount
FROM(SELECT visited_on,amount,
  lag(amount, 1) over() AS amount1,
  lag(amount, 2) over() AS amount2,
  lag(amount, 3) over() AS amount3,
  lag(amount, 4) over() AS amount4,
  lag(amount, 5) over() AS amount5,
  lag(amount, 6) over() AS amount6
  FROM (SELECT visited_on, SUM(amount) AS amount FROM Customer GROUP BY 1) AS temp2
  GROUP BY 1) AS temp
GROUP BY 1
HAVING visited_on >= date_add((SELECT visited_on FROM Customer LIMIT 1), INTERVAL 6 day)
ORDER BY 1;