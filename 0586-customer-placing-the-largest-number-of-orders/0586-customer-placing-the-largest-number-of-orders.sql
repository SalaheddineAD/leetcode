# Write your MySQL query statement below
# select customer_number
# from (select customer_number, count(order_number) as count_order
#     from orders
#     group by customer_number) as tb
# having count_order in (select max(count_order) from tb)

# select customer_number from (select customer_number,count(*) as ff from orders group by customer_number order by ff desc  limit 1) tt

with tb as (select customer_number, count(order_number) as maxi from Orders group by customer_number)
select customer_number from tb where maxi=(select max(maxi) from tb)
