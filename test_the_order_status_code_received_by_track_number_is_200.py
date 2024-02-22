# Руслан Бикмуллин, 13-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data
import pytest


# Функция создания нового заказа
def post_create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body)


post_create_new_order(data.order_body)


# Функция получения номера трека
def getting_track_number():
    # В переменную response сохраняется ответ полученный при создании нового заказа
    response = post_create_new_order(data.order_body)
    return response.json()["track"]


# В переменную track_number сохраняется номер трека
track_number = getting_track_number()


# Функция получения заказа по номеру трека
def get_order_by_track_number():
    parameter = {"t": track_number}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_NUMBER_PATH, params=parameter)


get_order_by_track_number()


# Проверка, что код ответа на запрос получения заказа по номеру трека равен 200

def test_the_order_status_code_received_by_track_number_is_200():
    # В переменную order сохраняется результат запроса на получение заказа по номеру трека:
    order = get_order_by_track_number()
    # Проверяется, что код ответа равен 200
    assert order.status_code == 200
