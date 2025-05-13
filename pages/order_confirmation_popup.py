import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderConfirmation(BasePage):
    CONFIRMATION_POPUP = "//section[contains(@class, 'Modal_modal_opened')]"
    CONFIRMATION_POPUP_HEADER = "//h2[contains(@class, 'Modal_modal__title_shadow') and contains(@class, 'text text_type_digits')]"
    CONFIRMATION_POPUP_NUMBER_LABEL = "идентификатор заказа"
    CONFIRMATION_POPUP_OVERLAY = "//div[contains(@class, 'Modal_modal_opened')]"
    CONFIRMATION_POPUP_X_BUTTON = "//section[contains(@class, 'Modal_modal__')]//button[@type='button']"
    CONFIRMATION_POPUP_DEFAULT_NUMBER = "//h2[normalize-space()='9999']"

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        self.wait_for_element_to_be_invisible(self.CONFIRMATION_POPUP_DEFAULT_NUMBER)
        self.wait_for_timeout(3)
        element = self.get_element_by_value(self.CONFIRMATION_POPUP_NUMBER_LABEL)
        previous_element = element.find_element(By.XPATH, "preceding-sibling::*")

        return previous_element.text

    @allure.step('Закрыть модальное окно с подтверждением заказа по кнопке Х')
    def close_confirmation_popup_by_cross_button(self):
        self.wait_for_element_to_be_invisible(self.CONFIRMATION_POPUP_OVERLAY)
        self.wait_for_timeout(3)
        self.click_on_element_by_xpath(self.CONFIRMATION_POPUP_X_BUTTON)
