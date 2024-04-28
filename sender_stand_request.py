import configuration
import requests

# функция POST-запроса с созданием заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.Create_new_order, json=order_body)

# функция POST-запроса с получением номера заказа
def get_order_data(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_track_order, params=track)