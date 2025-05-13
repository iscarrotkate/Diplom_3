import allure


class TestOrders:

    @allure.title('Изменение счетчика булок')
    @allure.description(
        'Тест проверяет, что при добавлении булок в заказ, счетчик увеличивается при первом добавлении и не меняется '
        'при последющих')
    def test_(self, home_page):
        home_page.open_page_by_direct_url()

        first_bun = home_page.select_bun(0)
        second_bun = home_page.select_bun(1)

        assert home_page.get_ingredient_counter_value(first_bun) == '0'
        assert home_page.get_ingredient_counter_value(second_bun) == '0'

        home_page.add_ingredient_to_order(first_bun)
        assert home_page.get_ingredient_counter_value(first_bun) == '2'
        assert home_page.get_ingredient_counter_value(second_bun) == '0'

        home_page.add_ingredient_to_order(second_bun)
        assert home_page.get_ingredient_counter_value(first_bun) == '0'
        assert home_page.get_ingredient_counter_value(second_bun) == '2'

    @allure.title('Изменение счетчика соусов')
    @allure.description('Тест проверяет, что при добавлении соусов в заказ, счетчик увеличивается')
    def test_sauce_counter(self, home_page):
        home_page.open_page_by_direct_url()

        element = home_page.select_sauce()
        assert home_page.get_ingredient_counter_value(element) == '0'

        home_page.add_ingredient_to_order(element)
        assert home_page.get_ingredient_counter_value(element) == '1'

        home_page.add_ingredient_to_order(element)
        assert home_page.get_ingredient_counter_value(element) == '2'

    @allure.title('Изменение счетчика начинок')
    @allure.description('Тест проверяет, что при добавлении начинок в заказ, счетчик увеличивается')
    def test_topping_counter(self, home_page):
        home_page.open_page_by_direct_url()

        element = home_page.select_topping()
        assert home_page.get_ingredient_counter_value(element) == '0'

        home_page.add_ingredient_to_order(element)
        assert home_page.get_ingredient_counter_value(element) == '1'

        home_page.add_ingredient_to_order(element)
        assert home_page.get_ingredient_counter_value(element) == '2'

    @allure.title('Открытие модального окна с детальной информацией об ингредиенте')
    @allure.description('Тест проверяет, что при клике на ингредиент открывается модальное окно с его описанием')
    def test_open_ingredient_details_popup(self, home_page, ingredient_details_popup):
        home_page.open_page_by_direct_url()

        ingredient = home_page.select_topping()

        ingredient_name = home_page.get_ingredient_list_name(ingredient)

        home_page.click_on_element(ingredient)

        assert ingredient_details_popup.get_ingredient_popup_name() == ingredient_name
        assert ingredient_details_popup.element_is_displayed_by_xpath(ingredient_details_popup.DETAILS_POPUP)
        assert ingredient_details_popup.element_is_displayed_by_xpath(ingredient_details_popup.DETAILS_POPUP_HEADER)
        assert ingredient_details_popup.element_is_displayed_by_xpath(ingredient_details_popup.DETAILS_POPUP_ENERGY_VALUE)

    @allure.title('Закрытие модального окна с детальной информацией об ингредиенте по кнопке Х')
    @allure.description('Тест проверяет, что при клике на кнопку Х закрывается модальное окно с его описанием')
    def test_close_ingredient_details_popup(self, home_page, ingredient_details_popup):
        home_page.open_page_by_direct_url()

        ingredient = home_page.select_topping()

        home_page.click_on_element(ingredient)

        assert home_page.element_is_displayed_by_xpath(ingredient_details_popup.DETAILS_POPUP)

        ingredient_details_popup.close_details_popup_by_cross_button()

        home_page.wait_for_timeout(3)

        assert not home_page.element_is_displayed_by_xpath(ingredient_details_popup.DETAILS_POPUP)

    @allure.title('Оформление заказа авторизованным пользователем')
    @allure.description('Тест проверяет, что при клике на кнопку Х закрывается модальное окно с его описанием')
    def test_place_order_by_authorized_user(self, login_page, home_page, new_user, order_confirmation_popup):
        login_page.open_page_by_direct_url()
        login_page.authorize(new_user)

        home_page.place_order()

        assert home_page.element_is_displayed_by_xpath(order_confirmation_popup.CONFIRMATION_POPUP)
        assert home_page.element_is_displayed_by_xpath(order_confirmation_popup.CONFIRMATION_POPUP_HEADER)
