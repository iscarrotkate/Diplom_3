from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls.urls import BASE_URL, ORDER_HISTORY_URL
import allure

class OrderHistoryPage(BasePage):
    page_url = f'{BASE_URL}{ORDER_HISTORY_URL}'

    ORDERS = "//ul[contains(@class, 'OrderHistory_profileList')]"
    ORDERS_LIST = "//li[contains(@class, 'OrderHistory_listItem')]"
    ORDER_NUMBER = ".//p[contains(@class, 'text text_type_digits-default')]"


    @allure.step('Получить заказ')
    def get_order_by_index(self, index=0):
        orders = self.get_list_of_elements_by_xpath(self.ORDERS_LIST)

        return orders[index]

    @allure.step('Получить номер заказа')
    def get_order_number_by_index(self, index=0):
        order = self.get_order_by_index(index)
        return order.find_element(By.XPATH, self.ORDER_NUMBER).text
