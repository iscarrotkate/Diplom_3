from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from urls.urls import BASE_URL
import allure


class HomePage(BasePage):
    page_url = f'{BASE_URL}/'

    CONSTRUCTOR_HEADER = "//h1[contains(text(),'Соберите бургер')]"
    CONSTRUCTOR = "//ul[@class='BurgerConstructor_basket__list__l9dp_']"
    INGREDIENTS_LIST = ".//a[contains(@class, 'BurgerIngredient_ingredient')]"
    INGREDIENTS_COUNTER = ".//p[contains(@class, 'counter_counter__num')]"
    INGREDIENT_NAME = ".//p[contains(@class, 'BurgerIngredient_ingredient__text')]"
    BUNS_SECTION = "//h2[text()='Булки']/following-sibling::ul[1]"
    SAUCES_SECTION = "//h2[text()='Соусы']/following-sibling::ul[1]"
    TOPPINGS_SECTION = "//h2[text()='Начинки']/following-sibling::ul[1]"
    PLACE_ORDER_BUTTON = "//button[contains(text(),'Оформить заказ')]"


    @allure.step('Открыть главную страницу')
    def open_page_by_direct_url(self):
        super().open_page_by_direct_url(self.page_url)

    @allure.step('Выбрать ингредиент')
    def select_ingredient(self, section, index):
        section = self.get_element_by_xpath(section)

        section_ingredients = self.get_child_elements_by_xpath(section, self.INGREDIENTS_LIST)

        return section_ingredients[index]

    @allure.step('Получить значение счетчика ингредиента')
    def get_ingredient_counter_value(self, ingredient):
        counter = ingredient.find_element(By.XPATH, self.INGREDIENTS_COUNTER)
        return counter.text

    @allure.step('Добавить ингредиент в заказ')
    def add_ingredient_to_order(self, element):
        target = self.get_element_by_xpath(self.CONSTRUCTOR)
        self.drag_and_drop_element(element, target)

    @allure.step('Выбрать булку')
    def select_bun(self, index=0):
        return self.select_ingredient(self.BUNS_SECTION, index)

    @allure.step('Выбрать соус')
    def select_sauce(self, index=0):
        return self.select_ingredient(self.SAUCES_SECTION, index)

    @allure.step('Выбрать начинку')
    def select_topping(self, index=0):
        return self.select_ingredient(self.TOPPINGS_SECTION, index)

    @allure.step('Получить имя ингредиента из списка ингредиентов')
    def get_ingredient_list_name(self, ingredient):
        return ingredient.find_element(By.XPATH, self.INGREDIENT_NAME).text

    @allure.step('Кликнуть по кнопке оформления заказа')
    def click_place_order_button(self):
        self.click_on_element_by_xpath(self.PLACE_ORDER_BUTTON)

    @allure.step('Оформить заказ')
    def place_order(self):
        bun = self.select_bun()
        self.add_ingredient_to_order(bun)

        sauce = self.select_sauce()
        self.add_ingredient_to_order(sauce)

        topping = self.select_topping()
        self.add_ingredient_to_order(topping)

        self.click_place_order_button()

