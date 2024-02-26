import requests
import data
import configuration


# Функция создания нового заказа
def create_order(body_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=body_order)


# Функция получения трека
def get_track():
    response_create_order = create_order(data.body_create_order)
    track = {"t": response_create_order.json()["track"]}
    return track


# Функция получения заказа по номеру трека
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_NUMBER_PATH, params=track)
