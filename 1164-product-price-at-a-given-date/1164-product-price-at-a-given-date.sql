WITH recent_products AS(
SELECT product_id, new_price AS price,
    ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) as rn
FROM products
    WHERE change_date <= "2019-08-16"
),

distinct_prods AS (
SELECT DISTINCT product_id
FROM products
)

SELECT d.product_id, IFNULL(r.price,10) AS price
FROM distinct_prods d
LEFT JOIN recent_products r
ON d.product_id = r.product_id AND  r.rn =1