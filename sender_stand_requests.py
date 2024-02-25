import requests
import data
import configuration


# Функция создания нового заказа
def post_create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)


post_create_new_order(data.order_body)