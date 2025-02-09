import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from constants import Constants
from locators import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Нажимаем на кнопку "Восстановить пароль"')
    def click_forgot_button(self):
        self.find_element(locator=Locators.BUTTON_FORGOT_PASSWORD).click()

    @allure.step('Ищем поле ввода почты и вводим почту')  # декоратор
    def text_field_email(self, email):
        self.find_element(locator=Locators.EMAIL_FIELD).send_keys(email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_recover_button(self):
        self.find_element(locator=Locators.BUTTON_RECOVER).click()

    @allure.step('Ищем поле ввода пароля и вводим пароль')
    def text_field_password(self, password):
        self.find_element(locator=Locators.PASSWORD_FIELD).send_keys(password)

    @allure.step('Нажимаем кнопку показать пароль')
    def click_show_button(self):
        hide = self.find_element(locator=Locators.SHOW_PASSWORD_BUTTON)
        hide.click()








