from pages.base_page import BasePage
from urls.urls import BASE_URL, PASSWORD_RESET_URL
import allure

class PasswordResetPage(BasePage):
    page_url = f'{BASE_URL}{PASSWORD_RESET_URL}'

    NEW_PASSWORD_INPUT = "//input[@name='Введите новый пароль']"
    NEW_PASSWORD_FIELD = "//div[contains(@class, 'input_type_password')]"
    RECOVERY_CODE_INPUT = "//input[@name='name']"
    HIDE_DISPLAY_BUTTON = "//div[@class='input__icon input__icon-action']//*[name()='svg']"

    @allure.step('Кликнуть по кнопку "Скрыть/показать" пароль')
    def click_on_eye_button(self):
        self.click_on_element_by_xpath(self.HIDE_DISPLAY_BUTTON)