from helpers.api_requests.base_client import HttpMethods


class OrderClient:
    ORDER_ENDPOINT = "/api/orders"

    def __init__(self, http_client):
        self.http_client = http_client

    def create_order(self, order_data, headers=None):
        return self.http_client.send_request(HttpMethods.POST, self.ORDER_ENDPOINT, data=order_data, headers=headers)
