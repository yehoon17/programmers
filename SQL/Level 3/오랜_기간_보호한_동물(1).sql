SELECT *
FROM (
    SELECT name, datetime
    FROM animal_ins
    WHERE animal_id IN (
        SELECT animal_id
        FROM ANIMAL_INS
        MINUS
        SELECT animal_id
        FROM ANIMAL_OUTS
        )
    ORDER BY datetime
)
WHERE ROWNUM < 4
