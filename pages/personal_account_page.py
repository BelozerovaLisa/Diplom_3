import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from constants import Constants
from locators import Locators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_personal_account(self):
        self.find_element(locator=Locators.BUTTON_PERSONAL_ACCOUNT).click()

    @allure.step('Ищем поле ввода почты и вводим почту')  # декоратор
    def text_field_email(self, email):
        self.find_element(locator=Locators.EMAIL_FIELD).send_keys(email)

    @allure.step('Ищем поле ввода пароля и вводим пароль')  # декоратор
    def text_field_password(self, password):
        self.find_element(locator=Locators.PASSWORD_FIELD).send_keys(password)

    @allure.step('Логинимся по кнопку Вход')
    def click_enter_button(self):
        self.find_element(locator=Locators.BUTTON_ENTER).click()

    @allure.step('Переход в раздел «История заказов»')
    def click_order_history(self):
        self.find_element(locator=Locators.BUTTON_ORDER_HISTORY).click()

    @allure.step('Выход из аккаунта')
    def log_out(self):
        self.find_element(locator=Locators.BUTTON_EXIT).click()


