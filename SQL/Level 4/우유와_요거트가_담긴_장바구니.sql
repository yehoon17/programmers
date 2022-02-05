SELECT cart_id
FROM cart_products
WHERE name = 'Yogurt'
AND cart_id IN (
    SELECT cart_id
    FROM cart_products
    WHERE name = 'Milk'
    )
