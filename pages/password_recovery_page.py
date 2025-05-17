from pages.base_page import BasePage
from urls.urls import BASE_URL, PASSWORD_RECOVERY_URL
import allure

class PasswordRecoveryPage(BasePage):
    page_url = f'{BASE_URL}{PASSWORD_RECOVERY_URL}'

    HEADER = "//h2[contains(text(),'Восстановление пароля')]"
    EMAIL_INPUT = "//input[@name='name']"
    RECOVER_BUTTON = "//button[contains(text(),'Восстановить')]"
    LOGIN_LINK = "//a[contains(text(),'Войти')]"
    NEW_PASSWORD_INPUT = "//input[@name='Введите новый пароль']"
    RECOVERY_CODE_INPUT = "//input[@name='name']"

    @allure.step('Открыть страницу восстановления пароля')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Ввести email для отправки запроса на восстановление доступа')
    def fill_email_input_with_value(self, value):
        self.fill_input_element_with_value(self.EMAIL_INPUT, value)

    @allure.step('Кликнуть по кнопке "Восстановить"')
    def click_on_recover_button(self):
        self.click_on_element_by_xpath(self.RECOVER_BUTTON)