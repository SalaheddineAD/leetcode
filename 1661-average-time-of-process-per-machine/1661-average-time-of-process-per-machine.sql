SELECT machine_id, 
round(2*AVG(CASE WHEN activity_type = 'end' THEN timestamp ELSE -timestamp END),3) as processing_time
FROM activity
GROUP BY machine_id

