# # Write your MySQL query statement below
# SELECT product_id, p.year as first_year, quantity , price
# FROM sales p
# GROUP BY product_id
# HAVING (product_id, p.year) IN (
#     SELECT product_id, min(p2.year)
#     FROM sales p2
#     GROUP BY product_id
#     )
    
    # Write your MySQL query statement below
SELECT product_id, year AS first_year, quantity, price 
FROM sales
WHERE (product_id, year) IN (
    SELECT product_id, MIN(year) 
    FROM sales 
    GROUP BY product_id
);