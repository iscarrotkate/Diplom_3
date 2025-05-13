import allure


class TestOrdersFeed:
    @allure.title('Открытие деталей заказа')
    @allure.description('Тест проверяет, что при клике по заказу в ленте заказов открывается модальное окно с информацией о заказе')
    def test_open_order_details(self, orders_feed, order_details_popup):

        orders_feed.open_page_by_direct_url()

        order = orders_feed.get_order()

        number = orders_feed.get_order_number(order)
        name = orders_feed.get_order_name(order)
        amount = orders_feed.get_order_amount(order)
        date = orders_feed.get_order_date(order)

        orders_feed.click_on_element(order)

        popup = order_details_popup.get_order_details_popup()

        assert order_details_popup.is_element_with_text_present(name, popup)
        assert order_details_popup.is_element_with_text_present(number, popup)
        assert order_details_popup.is_element_with_text_present(amount, popup)
        assert order_details_popup.is_element_with_text_present(date, popup)
        assert order_details_popup.element_is_displayed_by_xpath(order_details_popup.ORDER_COMPOSITION)

    @allure.title('Отображение заказов пользователя в ленте заказов')
    @allure.description('Тест проверяет, что номер заказа, представленный в списке заказов пользователя, представлен в ленте заказов')
    def test_user_orders_displayed_in_orders_feed(self, login_page, header, user_with_orders, order_history_page, profile_page, orders_feed):

        login_page.open_page_by_direct_url()
        login_page.authorize(user_with_orders)

        header.click_on_profile_button()

        profile_page.click_on_order_history_menu_item()

        order_number = order_history_page.get_order_number_by_index(0)

        header.click_on_orders_feed_button()

        assert orders_feed.is_element_with_text_present(order_number)


    @allure.title('Увеличение счетчика заказов за все время при оформлении заказов')
    @allure.description('Тест проверяет, что количество заказов за все время увеличивается при оформлении новых заказов')
    def test_total_order_counter_increase(self, order_confirmation_popup, login_page, header, new_user, home_page, order_history_page, profile_page, orders_feed):

        login_page.open_page_by_direct_url()
        login_page.authorize(new_user)

        header.click_on_orders_feed_button()
        initial_total_qnt = orders_feed.get_total_orders_qnt()

        header.click_on_constructor_button()

        home_page.place_order()

        order_confirmation_popup.close_confirmation_popup_by_cross_button()

        header.click_on_orders_feed_button()

        new_total_qnt = orders_feed.get_total_orders_qnt()

        assert new_total_qnt > initial_total_qnt

    @allure.title('Увеличение счетчика заказов за все сегодня при оформлении заказов')
    @allure.description(
        'Тест проверяет, что количество заказов за сегодня время увеличивается при оформлении новых заказов')
    def test_todays_order_counter_increase(self, order_confirmation_popup, login_page, header, new_user, home_page, order_history_page,
                                                  profile_page, orders_feed):
        login_page.open_page_by_direct_url()
        login_page.authorize(new_user)

        header.click_on_orders_feed_button()
        initial_total_qnt = orders_feed.get_todays_orders_qnt()

        header.click_on_constructor_button()

        home_page.place_order()

        order_confirmation_popup.close_confirmation_popup_by_cross_button()

        header.click_on_orders_feed_button()

        new_total_qnt = orders_feed.get_todays_orders_qnt()

        assert new_total_qnt > initial_total_qnt

    @allure.title('Отображение новых заказов в списке заказов в работе')
    @allure.description(
        'Тест проверяет, что номер нового заказа отображается в разделе "В работе"')
    def test_new_orders_displayed_in_orders_in_progress_list(self, order_confirmation_popup, login_page, header, new_user, home_page, order_history_page,
                                                  profile_page, orders_feed):
        login_page.open_page_by_direct_url()
        login_page.authorize(new_user)

        header.click_on_orders_feed_button()

        header.click_on_constructor_button()

        home_page.place_order()

        order_number = f'0{order_confirmation_popup.get_order_number()}'

        order_confirmation_popup.close_confirmation_popup_by_cross_button()

        header.click_on_orders_feed_button()

        orders_in_progress = orders_feed.get_orders_in_progress_list()
        assert order_number in orders_in_progress
