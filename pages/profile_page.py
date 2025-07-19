from pages.base_page import BasePage
from urls.urls import BASE_URL, PROFILE_URL
import allure

class ProfilePage(BasePage):
    page_url = f'{BASE_URL}{PROFILE_URL}'

    NAME_INPUT = "//label[contains(text(),'Имя')]/following-sibling::input"
    LOGIN_INPUT = "//label[contains(text(),'Логин')]/following-sibling::input"
    PASSWORD_INPUT = "//label[contains(text(),'Пароль')]/following-sibling::input"
    ORDER_HISTORY_BUTTON = "//a[contains(text(),'История заказов')]"
    EXIT_BUTTON = "//button[contains(text(),'Выход')]"

    @allure.step('Открыть страницу личного кабинета по прямому url')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Кликнуть по разделу "История заказов" в меню')
    def click_on_order_history_menu_item(self):
        self.click_on_element_by_xpath(self.ORDER_HISTORY_BUTTON)


    @allure.step('Кликнуть по кнопке "Выход"')
    def click_on_exit_button(self):
        self.click_on_element_by_xpath(self.EXIT_BUTTON)