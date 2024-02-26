# Руслан Бикмуллин, 13-я когорта — Финальный проект. Инженер по тестированию плюс

import pytest
import sender_stand_requests


# Проверка, что код ответа на запрос получения заказа по номеру трека равен 200
def test_the_order_status_code_received_by_track_is_200():
    # Получается трек
    response_get_track = sender_stand_requests.get_track()
    # Создается заказ по треку
    response_get_order_by_track = sender_stand_requests.get_order_by_track(response_get_track)
    assert response_get_order_by_track.status_code == 200
