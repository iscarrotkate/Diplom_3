import allure

from pages.base_page import BasePage


class IngredientDetails(BasePage):
    DETAILS_POPUP = "//div[contains(@class, 'Modal_modal__container') and not(@style = 'visibility: hidden')]"
    DETAILS_POPUP_HEADER = "//h2[contains(text(),'Детали ингредиента')]"
    DETAILS_POPUP_NAME = "//p[contains(@class, 'text text_type_main-medium')]"
    DETAILS_POPUP_ENERGY_VALUE = "//ul[contains(@class, 'Modal_modal__statsList')]"
    DETAILS_POPUP_X_BUTTON = "//section[contains(@class, 'Modal_modal_opened_')]//button[@type='button']"


    @allure.step('Получить имя ингредиента из модального окна')
    def get_ingredient_popup_name(self):
        return self.get_element_by_xpath(self.DETAILS_POPUP_NAME).text

    @allure.step('Закрыть модальное окно с детальной информацией об ингредиенте по кнопке Х')
    def close_details_popup_by_cross_button(self):
        self.click_on_element_by_xpath(self.DETAILS_POPUP_X_BUTTON)
