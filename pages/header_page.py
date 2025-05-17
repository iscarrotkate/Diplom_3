from pages.base_page import BasePage
import allure


class HeaderPage(BasePage):
    ACCOUNT_BUTTON = "//p[contains(text(),'Личный Кабинет')]"
    CONSTRUCTOR_BUTTON = "//p[contains(text(),'Конструктор')]"
    ORDERS_FEED_BUTTON = "//p[contains(text(),'Лента Заказов')]"

    @allure.step('Кликнуть по кнопке "Личный Кабинет"')
    def click_on_profile_button(self):
        self.click_on_element_by_xpath(self.ACCOUNT_BUTTON)

    @allure.step('Кликнуть по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.click_on_element_by_xpath(self.CONSTRUCTOR_BUTTON)

    @allure.step('Кликнуть по кнопке "Лента заказов"')
    def click_on_orders_feed_button(self):
        self.click_on_element_by_xpath(self.ORDERS_FEED_BUTTON)
