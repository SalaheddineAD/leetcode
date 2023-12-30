with first_order as (
    SELECT customer_id, MIN(order_date) as order_date
FROM delivery
    GROUP BY customer_id
)

SELECT ROUND(100*AVG(d.order_date = d.customer_pref_delivery_date), 2) AS immediate_percentage
FROM delivery d
INNER JOIN first_order f
ON d.customer_id = f.customer_id and f.order_date = d.order_date;