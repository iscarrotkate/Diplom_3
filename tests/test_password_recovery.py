import allure

from helpers.generators import generate_email
from pages.styles import DEFAULT_BORDER_COLOUR, ACTIVE_BORDER_COLOUR


class TestPasswordRecovery:

    @allure.title('Открытие страницы восстановления пароля')
    @allure.description(
        'В тесте проверяется, что при клике по кнопке "Восстановить пароль" на странице авторизации открывается страница восстановления пароля')
    def test_navigate_password_recovery_page(self, driver, login_page, password_recovery_page):
        login_page.open_page_by_direct_url()
        login_page.click_on_password_recovery_link()

        assert password_recovery_page.element_is_displayed_by_xpath(password_recovery_page.HEADER)
        assert driver.current_url == password_recovery_page.page_url

    @allure.title('Отправка запроса на восстановление пароля')
    @allure.description('Тест проверяет открытие формы восстановления пароля при отправке запроса на восстановление')
    def test_send_password_recovery_request(self, driver, password_recovery_page, password_reset_page):
        password_recovery_page.open_page_by_direct_url()
        password_recovery_page.fill_email_input_with_value(generate_email())
        password_recovery_page.click_on_recover_button()

        assert password_reset_page.element_is_displayed_by_xpath(password_recovery_page.NEW_PASSWORD_INPUT)
        assert password_reset_page.element_is_displayed_by_xpath(password_recovery_page.RECOVERY_CODE_INPUT)
        assert driver.current_url == password_reset_page.page_url

    @allure.title('Клик по кнопке "Показать/скрыть пароль" подсвечивает/скрывает подсветку поля для ввода')
    @allure.description(
        'Тест проверяет, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_eye(self, password_recovery_page, password_reset_page):
        password_recovery_page.open_page_by_direct_url()
        password_recovery_page.fill_email_input_with_value(generate_email())
        password_recovery_page.click_on_recover_button()

        password_reset_page.wait_for_element_to_be_visible(password_reset_page.NEW_PASSWORD_FIELD)
        field = password_reset_page.get_element_by_xpath(password_reset_page.NEW_PASSWORD_FIELD)

        assert password_reset_page.get_element_border_color(field) == DEFAULT_BORDER_COLOUR

        password_reset_page.click_on_eye_button()
        assert password_reset_page.get_element_border_color(field) == ACTIVE_BORDER_COLOUR

        password_reset_page.click_on_eye_button()
        assert password_reset_page.get_element_border_color(field) == DEFAULT_BORDER_COLOUR
