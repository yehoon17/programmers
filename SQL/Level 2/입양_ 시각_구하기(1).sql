SELECT to_number(hour) as hour, count(hour) as count
FROM (
    SELECT to_char(datetime, 'HH24') as hour
    FROM animal_outs
    )
WHERE to_number(hour) BETWEEN 9 AND 19
GROUP BY hour
ORDER BY hour
