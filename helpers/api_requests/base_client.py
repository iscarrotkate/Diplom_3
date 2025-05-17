from enum import Enum
import allure
import requests


class HttpMethods(str, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class HttpClient:

    def __init__(self, url):
        self.base_url = url

    def send_request(self, method: HttpMethods, endpoint: str, data=None, headers=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        request_kwargs = {}

        if data:
            request_kwargs["data"] = data
        if headers:
            request_kwargs["headers"] = headers

        request_kwargs.update(kwargs)

        try:
            with allure.step(f"Отправить запрос {method} по {url}"):
                return requests.request(method, url, **request_kwargs)
        except requests.RequestException as e:
            return f"Запрос {method} не был отправлен по {url}. Ошибка: {e}"
