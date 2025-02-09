import allure
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver
from constants import Constants
from locators import Locators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    @allure.step('Нажимаем на первы заказ в списке"')
    def click_order_on_list(self):
        self.find_element(locator=Locators.ORDER_FIELD).click()

    
