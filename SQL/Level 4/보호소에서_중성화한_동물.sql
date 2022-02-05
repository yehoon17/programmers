SELECT ins.animal_id, ins.animal_type, ins.name
FROM ANIMAL_INS ins, ANIMAL_OUTS outs
WHERE ins.animal_id = outs.animal_id AND sex_upon_intake LIKE '%Intact%'
                                     AND NOT sex_upon_outcome LIKE '%Intact%'
