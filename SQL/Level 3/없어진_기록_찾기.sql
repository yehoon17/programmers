SELECT outs.animal_id, name
FROM
(
SELECT animal_id
FROM ANIMAL_OUTS
MINUS
SELECT animal_id
FROM ANIMAL_INS) missing, ANIMAL_OUTS outs
WHERE missing.animal_id = outs.animal_id
ORDER BY outs.animal_id
