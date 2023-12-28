-- Write your PostgreSQL query statement below
SELECT p.product_name, s.year, s.price
FROM product p inner join sales s
on s.product_id = p.product_id