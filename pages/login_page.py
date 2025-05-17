from pages.base_page import BasePage
from urls.urls import BASE_URL, LOGIN_URL
import allure

class LoginPage(BasePage):
    page_url = f'{BASE_URL}{LOGIN_URL}'

    PASSWORD_RECOVERY_LINK = "//a[contains(text(),'Восстановить пароль')]"
    EMAIL_INPUT = "//input[@name='name']"
    PASSWORD_INPUT = "//input[@name='Пароль']"
    LOGIN_BUTTON = "//button[contains(text(),'Войти')]"
    HEADER = "//h2[contains(text(),'Вход')]"

    @allure.step('Открыть страницу авторизации')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Кликнуть по ссылке "Восстановление пароля"')
    def click_on_password_recovery_link(self):
        self.click_on_element_by_xpath(self.PASSWORD_RECOVERY_LINK)


    @allure.step('Кликнуть по ссылке "Войти"')
    def click_on_login_button(self):
        self.click_on_element_by_xpath(self.LOGIN_BUTTON)

    @allure.step('Заполнить форму авторизации')
    def fill_in_login_form(self, login_data):
        self.fill_input_element_with_value(self.EMAIL_INPUT, login_data["email"])
        self.fill_input_element_with_value(self.PASSWORD_INPUT, login_data["password"])

    @allure.step('Авторизоваться')
    def authorize(self, login_data):
        self.fill_input_element_with_value(self.EMAIL_INPUT, login_data["email"])
        self.fill_input_element_with_value(self.PASSWORD_INPUT, login_data["password"])
        self.click_on_login_button()