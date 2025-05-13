import allure


class TestNavigation:

    @allure.title('Открытие страницы конструктора')
    @allure.description('В тесте проверяется, что при клике по кнопке "Конструктор" открывается главная страница')
    def test_navigate_to_consructor(self, login_page, header, home_page):
        login_page.open_page_by_direct_url()
        header.click_on_constructor_button()

        assert home_page.element_is_displayed_by_xpath(home_page.CONSTRUCTOR_HEADER)
        assert home_page.current_url_is_expected(home_page.page_url)

    @allure.title('Открытие страницы ленты заказов')
    @allure.description(
        'В тесте проверяется, что при клике по кнопке "Лента заказов" открывается страница ленты заказов')
    def test_navigate_orders_feed(self, login_page, header, orders_feed):
        login_page.open_page_by_direct_url()
        header.click_on_orders_feed_button()

        assert orders_feed.element_is_displayed_by_xpath(orders_feed.FEED_HEADER)
        assert orders_feed.current_url_is_expected(orders_feed.page_url)
