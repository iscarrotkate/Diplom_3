import time

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить элемент по xpath')
    def get_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element(By.XPATH, xpath)
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Получить элемент по значению')
    def get_element_by_value(self, value):
        try:
            return self.driver.find_element(By.XPATH, f"//*[contains(text(), '{value}')]")
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Получить дочерние элементы по xpath')
    def get_child_elements_by_xpath(self, element, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return element.find_elements(By.XPATH, xpath)
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Получить список элементов по xpath')
    def get_list_of_elements_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_elements(By.XPATH, xpath)
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Ждать, пока элемент не станет кликабельным')
    def wait_for_element_to_be_clickable(self, element):
        try:
            return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Открыть страницу по прямому URL')
    def open_page_by_direct_url(self, url):
        self.driver.get(url)

    @allure.step('Получить URL текущей страницы')
    def get_current_page_url(self):
        return self.driver.current_url

    @allure.step('Проскролить страницу до элемента')
    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except Exception:
            raise Exception(f"Не удалось выполнить скролл")

    @allure.step('Проверить соответствие текущего URL ожидаемому')
    def current_url_is_expected(self, expected_url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(expected_url))
        return self.driver.current_url == expected_url

    @allure.step('Заполнить поле для ввода значением')
    def fill_input_element_with_value(self, xpath, value):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.find_element(By.XPATH, xpath).send_keys(value)
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Проверить отображается ли элемент')
    def element_is_displayed_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element(By.XPATH, xpath).is_displayed()
        except:
            return False

    @allure.step('Кликнуть по элементу')
    def click_on_element_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 15).until(
                expected_conditions.element_to_be_clickable((By.XPATH, xpath))
            ).click()
        except TimeoutError:
            raise Exception(f"Элемент не стал кликабелен в течение 15 секунд")

    @allure.step('Ждать, пока элемент не отобразится')
    def wait_for_element_to_be_visible(self, xpath):
        try:
            WebDriverWait(self.driver, 15).until(
                expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutError:
            return False

    @allure.step('Ждать, пока элемент не скроется')
    def wait_for_element_to_be_invisible(self, xpath):
        try:
            WebDriverWait(self.driver, 15).until(
                expected_conditions.invisibility_of_element_located((By.XPATH, xpath)))
            return True
        except TimeoutError:
            return False

    @allure.step('Ждать указанный таймаут')
    def wait_for_timeout(self, timeout):
        time.sleep(timeout)

    @allure.step('Установить access token')
    def set_access_token(self, token):
        self.driver.execute_script(f"localStorage.setItem('accessToken', '{token}');")

    @allure.step('Проверить, установлен ли access token')
    def access_token_is_set(self):
        return self.driver.execute_script("return localStorage.getItem('accessToken');")

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source, target):

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step('Кликнуть по элементу')
    def click_on_element(self, element):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(element))
            element.click()
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Проверить наличие элемента с текстом')
    def is_element_with_text_present(self, text, parent=None):
        context = parent if type(parent) == WebElement else self.driver
        try:
            element = WebDriverWait(context, 10).until(expected_conditions.visibility_of_element_located(
                (By.XPATH, f".//*[contains(., '{text}')]")))
            return text in element.text
        except Exception:
            return False


    @allure.step('Проверить цвет элемента')
    def get_element_color(self, element):
        try:
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(element))
            return element.value_of_css_property('color')
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")

    @allure.step('Проверить цвет рамки элемента')
    def get_element_border_color(self, element):
        try:
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(element))
            return element.value_of_css_property('border-color')
        except Exception:
            raise Exception(f"Не удалось определить видимость элемента")