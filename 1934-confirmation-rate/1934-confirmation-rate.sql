SELECT s.user_id, 
# ROUND(avg(if(c.action="confirmed",1,0)),2)
ROUND(SUM(if(c.action="confirmed",1,0))/COUNT(*),2) 
AS confirmation_rate
FROM signups s 
LEFT JOIN confirmations c
on s.user_id = c .user_id
GROUP BY s.user_id