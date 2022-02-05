SELECT ins.animal_id, ins.name
FROM ANIMAL_INS ins, ANIMAL_OUTS outs
WHERE ins.animal_id = outs.animal_id AND ins.datetime > outs.datetime
ORDER BY ins.datetime
