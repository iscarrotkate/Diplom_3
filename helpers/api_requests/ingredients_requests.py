from helpers.api_requests.base_client import HttpMethods


class IngredientsClient:
    INGREDIENT_ENDPOINT = "/api/ingredients"

    def __init__(self, http_client):
        self.http_client = http_client

    def get_ingredients(self):
        return self.http_client.send_request(HttpMethods.GET, self.INGREDIENT_ENDPOINT)
