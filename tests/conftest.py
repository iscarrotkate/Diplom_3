import pytest
from selenium import webdriver

from helpers.api_requests.base_client import HttpClient
from helpers.api_requests.ingredients_requests import IngredientsClient
from helpers.api_requests.order_requests import OrderClient
from helpers.api_requests.user_requests import UserClient
from helpers.generators import generate_email, generate_random_string
from pages.header_page import HeaderPage
from pages.home_page import HomePage
from pages.ingredient_details_popup import IngredientDetails
from pages.login_page import LoginPage
from pages.order_confirmation_popup import OrderConfirmation
from pages.order_details_popup import OrderDetails
from pages.order_history_page import OrderHistoryPage
from pages.orders_feed_page import OrdersFeed
from pages.password_recovery_page import PasswordRecoveryPage
from pages.password_reset_page import PasswordResetPage
from pages.profile_page import ProfilePage
from urls.urls import BASE_URL


@pytest.fixture(params=("chrome", "firefox"))
def driver(request):
    browser = get_browser(request.param)
    try:
        yield browser
    finally:
        browser.quit()


def get_browser(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError("Неподдерживаемый браузер")


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def password_recovery_page(driver):
    return PasswordRecoveryPage(driver)


@pytest.fixture
def password_reset_page(driver):
    return PasswordResetPage(driver)


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def ingredient_details_popup(driver):
    return IngredientDetails(driver)


@pytest.fixture
def order_confirmation_popup(driver):
    return OrderConfirmation(driver)


@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)


@pytest.fixture
def order_history_page(driver):
    return OrderHistoryPage(driver)


@pytest.fixture
def header(driver):
    return HeaderPage(driver)


@pytest.fixture
def orders_feed(driver):
    return OrdersFeed(driver)


@pytest.fixture
def order_details_popup(driver):
    return OrderDetails(driver)


@pytest.fixture
def client():
    return HttpClient(BASE_URL)


@pytest.fixture
def user_client(client):
    return UserClient(client)


@pytest.fixture
def ingredients_client(client):
    return IngredientsClient(client)


@pytest.fixture
def order_client(client):
    return OrderClient(client)


@pytest.fixture
def ingredients(ingredients_client):
    ingredients = ingredients_client.get_ingredients().json()["data"]

    ingredients_ids = [ingredient["_id"] for ingredient in ingredients]

    return ingredients_ids


@pytest.fixture
def registration_data(client, user_client, request):
    email = generate_email()
    name = generate_random_string(10)
    password = generate_random_string(10)

    payload = {'email': email, 'password': password, 'name': name}
    user_client.register_request(payload)

    yield {
        "email": email,
        "name": name,
        "password": password
    }

    payload = {'email': email, 'password': password}

    token = user_client.login_request(payload).json()["accessToken"]
    user_client.delete_user_request(token)


@pytest.fixture
def user_with_orders(user_client, registration_data, order_client, ingredients):
    login_payload = {'email': registration_data["email"], 'password': registration_data["password"]}

    token = user_client.login_request(login_payload).json()["accessToken"]

    order_payload = {"ingredients": ingredients[:3]}
    header = {"authorization": token}

    [order_client.create_order(order_payload, header) for _ in range(5)]

    yield {
        "email": registration_data["email"],
        "name": registration_data["name"],
        "password": registration_data["password"],
        "token": token
    }


@pytest.fixture
def new_user(user_client, registration_data, order_client, ingredients):
    login_payload = {'email': registration_data["email"], 'password': registration_data["password"]}

    token = user_client.login_request(login_payload).json()["accessToken"]

    yield {
        "email": registration_data["email"],
        "name": registration_data["name"],
        "password": registration_data["password"],
        "token": token
    }
