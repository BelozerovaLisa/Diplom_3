import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from conftest import driver
from constants import Constants

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url_main = Constants.URL_MAIN
        self.url_login = Constants.URL_LOGIN
        self.url_forgot_password = Constants.URL_FORGOT_PASSWORD
        self.url_profile = Constants.URL_PROFILE
        self.url_order_feed = Constants.URL_ORDER_FEED

    @allure.step('Открываем страницу Stallar Burger')  # декоратор
    def go_to_site_main(self):
        self.driver.get(self.url_main)

    @allure.step('Открываем страницу авторизации')
    def go_to_site_login(self):
        self.driver.get(self.url_login)

    @allure.step('Открываем страницу восстановления пароля')
    def go_to_site_forgot_password(self):
        self.driver.get(self.url_forgot_password)

    @allure.step('Открываем страницу личного кабинета')
    def go_to_site_profile(self):
        self.driver.get(self.url_profile)

    @allure.step('Открываем страницу ленты заказов')
    def go_to_site_order_feed(self):
        self.driver.get(self.url_order_feed)

    @allure.step('Ищем элемент на странице')  # декоратор
    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find element {locator}')

    def drag_and_drop(self, source_locator, target_locator):
        wait = WebDriverWait(self.driver, 10)
        source = wait.until(EC.presence_of_element_located(source_locator))
        target = wait.until(EC.presence_of_element_located(target_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", source)
        actions = ActionChains(self.driver)
        actions.click_and_hold(source).move_to_element(target).release().perform()

    @allure.step('Ищем текст')
    def element_text(self, locator_param):
        question_text = self.find_element(locator=locator_param).text
        return question_text














