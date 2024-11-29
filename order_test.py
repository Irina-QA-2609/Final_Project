import data
from order_request import create_order, get_order


def test_create_order_and_get_order():
    order_response = create_order(data.order_body)
    assert order_response.status_code == 201

    track_number = order_response.json().get("track")
    assert track_number is not None

    data_order = get_order(track_number)
    assert data_order.status_code == 200
