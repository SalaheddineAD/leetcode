SELECT product_name, unit
FROM products INNER JOIN (
    SELECT  product_id, SUM(unit) AS unit
    FROM orders
    WHERE order_date BETWEEN "2020-02-01" AND '2020-02-29'
    GROUP BY product_id
    HAVING SUM(unit)>=100) AS S
ON s.product_id = products.product_id
