import allure
import pytest
from time import sleep

from constants import Constants
from locators import Locators
from pages.burger_page import BurgerPage
from pages.personal_account_page import PersonalAccountPage

@allure.title('Тестируем заказ бургеров')
class TestBurgerOrder:
    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_click_constructor_button(self,driver):
        order_burger = BurgerPage(driver)
        order_burger.go_to_site_order_feed()
        order_burger.click_constructor_button()
        assert driver.current_url == Constants.URL_CONSTRUCTOR

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_order_feed(self, driver):
        order_burger = BurgerPage(driver)
        order_burger.go_to_site_main()
        order_burger.click_order_feed_button()
        assert driver.current_url == Constants.URL_ORDER_FEED

    @allure.title('Проверка если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, driver):
        order_burger = BurgerPage(driver)
        order_burger.go_to_site_main()
        order_burger.click_ingredient()
        element = order_burger.element_text(Locators.TEXT_INGREDIENT)
        assert element == Constants.TEXT_INGREDIENT

    @allure.title('Проверка всплывающее окно закрывается кликом по крестику')
    def test_click_close(self, driver):
        order_burger = BurgerPage(driver)
        order_burger.go_to_site_main()
        order_burger.click_ingredient()
        order_burger.click_close()
        element = order_burger.element_text(Locators.TEXT_ON_MAIN_PAGE)
        assert element == Constants.TEXT_MAIN

    @allure.title('Проверка при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_counter_ingredients(self, driver):
        order_burger = BurgerPage(driver)
        order_burger.go_to_site_main()
        order_burger.drag_and_drop(Locators.FIRST_INGREDIENT, Locators.CONSTRUCTOR) # Для FireFox не работает перетягивание
        element = order_burger.element_text(Locators.INGREDIENTS_COUNTER)
        assert element == '2'

    @allure.title('Проверка что залогиненный пользователь может оформить заказ')
    def test_user_order(self, driver, prepare_user):
        order_burger = BurgerPage(driver)
        personal_account = PersonalAccountPage(driver)
        order_burger.go_to_site_login()
        personal_account.text_field_email(Constants.email)
        personal_account.text_field_password(Constants.password)
        personal_account.click_enter_button()
        order_burger.drag_and_drop(Locators.FIRST_INGREDIENT, Locators.CONSTRUCTOR)  # Для FireFox не работает перетягивание
        order_burger.click_place_order()
        element = order_burger.element_text(Locators.TEXT_ORDER_ID)
        assert element == Constants.TEXT_CREATE_ORDER






