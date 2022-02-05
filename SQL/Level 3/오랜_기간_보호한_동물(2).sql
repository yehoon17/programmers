SELECT animal_id, name
FROM (
    SELECT outs.animal_id, outs.name, outs.datetime - ins.datetime AS time
    FROM animal_ins ins, animal_outs outs
    WHERE ins.animal_id = outs.animal_id
    ORDER BY time DESC
    )
WHERE ROWNUM <= 2
