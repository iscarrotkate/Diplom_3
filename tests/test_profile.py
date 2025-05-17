import allure

from pages.styles import MENU_ITEM_SELECTED_COLOUR


class TestProfile:

    @allure.title('Открытие личного кабинета по кнопке "Личный кабинет" авторизованным пользователем')
    @allure.description(
        'В тесте проверяется, что при клике по кнопке "Личный кабинет" авторизованным пользователем открывается '
        'личный кабинет')
    def test_navigate_to_profile_by_authorized_user(self, header, user_with_orders, home_page, profile_page):
        home_page.open_page_by_direct_url()
        home_page.set_access_token(user_with_orders["token"])
        header.click_on_profile_button()

        assert profile_page.current_url_is_expected(profile_page.page_url)

        assert profile_page.get_element_by_xpath(profile_page.NAME_INPUT).get_attribute("value") == user_with_orders[
            'name']
        assert profile_page.get_element_by_xpath(profile_page.LOGIN_INPUT).get_attribute("value") == user_with_orders[
            'email']

    @allure.title('Открытие раздела "История заказов"')
    @allure.description(
        'В тесте проверяется, что при клике по кнопке "История заказов" открывается вкладка с историей заказов')
    def test_navigate_to_order_history_by_authorized_user(self, user_with_orders, profile_page, home_page,
                                                          order_history_page, header):
        home_page.open_page_by_direct_url()
        home_page.set_access_token(user_with_orders["token"])
        header.click_on_profile_button()

        profile_page.click_on_order_history_menu_item()
        button = profile_page.get_element_by_xpath(profile_page.ORDER_HISTORY_BUTTON)
        assert profile_page.get_element_color(button) == MENU_ITEM_SELECTED_COLOUR

        assert order_history_page.element_is_displayed_by_xpath(order_history_page.ORDERS)

        assert order_history_page.current_url_is_expected(order_history_page.page_url)

    @allure.title('Выход из профиля')
    @allure.description(
        'В тесте проверяется, что при клике по кнопке "Выход" удаляется авторизационных токен и происходит '
        'переаправление на страницу авторизации')
    def test_logout(self, user_with_orders, profile_page, login_page, header):
        login_page.open_page_by_direct_url()
        login_page.fill_in_login_form(user_with_orders)
        login_page.click_on_login_button()
        header.click_on_profile_button()

        profile_page.click_on_exit_button()

        login_page.wait_for_element_to_be_visible(login_page.HEADER)

        assert not profile_page.access_token_is_set()

        assert login_page.current_url_is_expected(login_page.page_url)
