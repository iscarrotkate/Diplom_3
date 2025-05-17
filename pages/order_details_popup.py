from selenium.common import NoSuchElementException

from pages.base_page import BasePage
import allure

class OrderDetails(BasePage):

    ORDER_POPUP = "//div[contains(@class, 'Modal_orderBox') and not(@style = 'visibility: hidden')]"
    ORDER_COMPOSITION = "//ul[@class='Modal_list__2sHWc']"


    @allure.step('Получить модальное окно с детальной информацией о заказе')
    def get_order_details_popup(self):
        try:
            return self.get_element_by_xpath(self.ORDER_POPUP)
        except NoSuchElementException:
            return "Модальное окно не найдено"


