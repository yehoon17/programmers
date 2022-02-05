SELECT id, name, a.host_id
FROM (
    SELECT host_id, COUNT(host_id) AS cnt
    FROM PLACES
    GROUP BY host_id
    ) a, PLACES b
WHERE cnt > 1 and a.host_id = b.host_id
ORDER BY id
