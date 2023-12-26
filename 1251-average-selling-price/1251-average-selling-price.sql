SELECT P.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM prices p
LEFT JOIN unitssold u
on p.product_id = u.product_id AND
u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;