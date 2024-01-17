# # Write your MySQL query statement below
# SELECT request_at as Day, 
#     ROUND(SUM(IF( t.status != 'completed' AND (drivers.banned ="Yes" OR clients.banned = 'Yes'),1,0)) /
#     SUM(IF ( drivers.banned = 'No' AND clients.banned = 'No',1,0)) ,2) AS "Cancellation Rate"
# FROM users drivers INNER JOIN trips t
# ON drivers.users_id = t.driver_id AND drivers.role = 'driver'
# INNER JOIN users clients 
# ON clients.users_id = t.client_id AND clients.role = 'client'
# WHERE t.request_at BETWEEN "2013-10-01" AND "2013-10-03"
# GROUP BY t.request_at

# Write your MySQL query statement below
SELECT request_at as Day, 
    ROUND(SUM(IF( t.status != 'completed',1,0)) / COUNT(*) ,2) AS "Cancellation Rate"
FROM users drivers INNER JOIN trips t
ON drivers.users_id = t.driver_id AND drivers.role = 'driver'
INNER JOIN users clients 
ON clients.users_id = t.client_id AND clients.role = 'client'
WHERE t.request_at BETWEEN "2013-10-01" AND "2013-10-03" 
    AND drivers.banned = 'No' AND clients.banned = 'No'
GROUP BY t.request_at