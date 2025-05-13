from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls.urls import BASE_URL, ORDERS_FEED
import allure

class OrdersFeed(BasePage):
    page_url = f'{BASE_URL}{ORDERS_FEED}'

    FEED_HEADER = "//h1[contains(text(),'Лента заказов')]"
    ORDERS_LIST = "//li[contains(@class, 'OrderHistory_listItem')]"
    ORDER_AMOUNT = ".//p[contains(@class, 'text text_type_digits-default mr-2')]"
    ORDER_NUMBER = ".//p[@class='text text_type_digits-default']"
    ORDER_NAME = ".//h2[@class='text text_type_main-medium mb-2']"
    ORDER_DATE = ".//p[contains(@class, 'text text_type_main-default')]"
    TOTAL_ORDERS = "//p[contains(text(),'Выполнено за все время:')]"
    TODAYS_ORDERS = "//p[contains(text(),'Выполнено за сегодня:')]"
    ORDERS_IN_PROGRESS = "//ul[contains(@class, 'OrderFeed_orderListReady')]"
    NO_ORDERS_IN_PROGRESS = "//li[normalize-space()='Все текущие заказы готовы!']"


    @allure.step('Открыть страницу ленты заказов')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Получить заказ')
    def get_order(self, index=0):
        orders = self.get_list_of_elements_by_xpath(self.ORDERS_LIST)

        return orders[index]

    @allure.step('Получить дату заказа')
    def get_order_date(self, order):
        return order.find_element(By.XPATH, self.ORDER_DATE).text


    @allure.step('Получить имя заказа')
    def get_order_name(self, order):
        return order.find_element(By.XPATH, self.ORDER_NAME).text

    @allure.step('Получить сумму заказа')
    def get_order_amount(self, order):
        return order.find_element(By.XPATH, self.ORDER_AMOUNT).text

    @allure.step('Получить номер заказа')
    def get_order_number(self, order):
        return order.find_element(By.XPATH, self.ORDER_NUMBER).text

    @allure.step('Получить количество заказов за все время')
    def get_total_orders_qnt(self):
        element = self.get_element_by_xpath(self.TOTAL_ORDERS)
        self.wait_for_timeout(3)
        next_element = element.find_element(By.XPATH, "following-sibling::p")

        return int(next_element.text)

    @allure.step('Получить количество заказов за все сегодня')
    def get_todays_orders_qnt(self):
        element = self.get_element_by_xpath(self.TODAYS_ORDERS)
        next_element = element.find_element(By.XPATH, "following-sibling::p")

        return int(next_element.text)

    @allure.step('Получить список заказов в работе')
    def get_orders_in_progress_list(self):

        #self.wait_for_element_to_be_invisible(self.NO_ORDERS_IN_PROGRESS)
        self.wait_for_timeout(5)
        orders_section = self.get_element_by_xpath(self.ORDERS_IN_PROGRESS)
        orders = orders_section.find_elements(By.XPATH, ".//*")

        if orders[0] == self.NO_ORDERS_IN_PROGRESS:
            return []
        else:
            return [order.text for order in orders]

    @allure.step('Получить элемент "В работе"')
    def get_in_progress_section(self):
        return self.get_element_by_xpath(self.ORDERS_IN_PROGRESS)
