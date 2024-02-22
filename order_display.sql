Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).


SELECT c.login,
       COUNT (o.track) AS count_orders
FROM "Orders" AS o
INNER JOIN "Couriers" AS c ON o."courierId" = c.id
WHERE "inDelivery" = TRUE
GROUP BY c.login;