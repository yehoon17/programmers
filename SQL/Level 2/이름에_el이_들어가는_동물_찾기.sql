SELECT animal_id, name
FROM animal_ins
WHERE LOWER(name) LIKE '%el%' AND animal_type = 'Dog'
ORDER BY name
