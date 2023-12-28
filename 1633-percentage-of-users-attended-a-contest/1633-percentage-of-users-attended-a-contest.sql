WITH nb_users AS (
SELECT COUNT(user_id)
FROM users
)

SELECT contest_id, ROUND(COUNT(user_id)*100/(SELECT COUNT(user_id)
FROM users),2) as percentage
FROM register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;