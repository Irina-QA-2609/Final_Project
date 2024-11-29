import configuration
import requests
import data

def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)
response = create_order(data.order_body)

def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track_number))