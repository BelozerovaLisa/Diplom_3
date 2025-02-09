import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from constants import Constants
from locators import Locators
from pages.base_page import BasePage


class BurgerPage(BasePage):
    @allure.step('Нажимаем на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.find_element(locator=Locators.BUTTON_CONSTRUCTOR).click()

    @allure.step('Нажимаем на кнопку "Лента заказов"')
    def click_order_feed_button(self):
        self.find_element(locator=Locators.BUTTON_ORDER_FEED).click()

    @allure.step('Нажимаем на кнопку "Лента заказов" и ждем когда появится нужный текст')
    def click_order_feed_button_with_text(self):
        self.find_element(locator=Locators.BUTTON_ORDER_FEED).click()
        WebDriverWait(self.driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")



    @allure.step('Нажимаем на первый ингредиент"')
    def click_ingredient(self):
        self.find_element(Locators.FIRST_INGREDIENT).click()


    @allure.step('Нажимаем на крестик')
    def click_close(self):
        self.find_element(locator=Locators.BUTTON_CLOSE).click()

    @allure.step('Нажимаем на кнопку оформить заказ')
    def click_place_order(self):
        self.find_element(locator=Locators.BUTTON_PLACE_ORDER).click()
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(Locators.SHADOW_FORM_ORDER))




