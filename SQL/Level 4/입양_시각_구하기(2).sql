SELECT a.hour, NVL(count, 0) FROM (SELECT ROWNUM-1 AS hour FROM dual CONNECT BY LEVEL < 25) a
LEFT JOIN (SELECT TO_CHAR(datetime, 'hh24') AS hour, COUNT(TO_CHAR(datetime, 'hh24')) AS count FROM ANIMAL_OUTS GROUP BY TO_CHAR(datetime, 'hh24')) b ON a.hour=b.hour
ORDER BY a.hour
