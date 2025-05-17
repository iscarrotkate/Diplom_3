from helpers.api_requests.base_client import HttpMethods


class UserClient:
    REGISTER_ENDPOINT = "/api/auth/register"
    USER_ENDPOINT = "/api/auth/user"
    LOGIN_ENDPOINT = "/api/auth/login"

    def __init__(self, http_client):
        self.http_client = http_client

    def register_request(self, registration_data):
        return self.http_client.send_request(HttpMethods.POST, self.REGISTER_ENDPOINT, data=registration_data)

    def login_request(self, login_data):
        return self.http_client.send_request(HttpMethods.POST, self.LOGIN_ENDPOINT, data=login_data)

    def delete_user_request(self, token):
        header = {"authorization": token}
        return self.http_client.send_request(HttpMethods.DELETE, self.USER_ENDPOINT, headers=header)
