# Руслан Бикмуллин, 13-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data
import pytest
import sender_stand_requests


# Функция получения номера трека
def getting_track_number():
    # В переменную response сохраняется ответ полученный при создании нового заказа
    response = sender_stand_requests.post_create_new_order(data.order_body)
    return response.json()["track"]


# В переменную received_track_number сохраняется полученный номер трека
received_track_number = getting_track_number()


# Функция получения заказа по номеру трека
def get_order_by_track_number(track_number):
    # Меняется тип у переменной track_number с number на string
    str_track_number = str(track_number)
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_NUMBER_PATH + str_track_number)


get_order_by_track_number(received_track_number)


# Проверка, что код ответа на запрос получения заказа по номеру трека равен 200
def test_the_order_status_code_received_by_track_number_is_200():
    # В переменную order сохраняется результат запроса на получение заказа по номеру трека:
    order = get_order_by_track_number(received_track_number)
    # Проверяется, что код ответа равен 200
    assert order.status_code == 200
