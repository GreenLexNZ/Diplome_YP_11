import sender_stand_request
import data

# Создание и проверка статуса заказа
def test_status_order_200():
    response = sender_stand_request.post_new_order(data.order_body)
    track = {"t": response.json()["track"]}
    response_track = sender_stand_request.get_order_data(track)
    assert response_track.status_code == 200

