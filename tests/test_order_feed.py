import allure
import pytest
from time import sleep


from selenium import webdriver
from constants import Constants
from locators import Locators
from pages.burger_page import BurgerPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage

@allure.title('Тестируем ленту заказов')
class TestOrderFeed:
    @allure.title('Проверка при нажатии на заказ открывется всплывающее окно с деталями')
    def test_click_order_on_list(self,driver):
        order_feed = OrderFeedPage(driver)
        order_feed.go_to_site_order_feed()
        order_feed.click_order_on_list()
        element = order_feed.element_text(Locators.TEXT_INGREDIENT_BURGER_ORDER)
        sleep(2)
        assert element == Constants.TEXT_STRUCTURE

    @allure.title('Проверка что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_check_order_on_order_feed(self,driver, prepare_user):
        order_burger = BurgerPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account = PersonalAccountPage(driver)
        order_burger.go_to_site_login()
        personal_account.text_field_email(Constants.email)
        personal_account.text_field_password(Constants.password)
        personal_account.click_enter_button()
        order_burger.drag_and_drop(Locators.FIRST_INGREDIENT,Locators.CONSTRUCTOR)  # Для FireFox не работает перетягивание
        sleep(2)
        order_burger.click_place_order()
        sleep(3)
        order_burger.click_close()
        order_burger.click_order_feed_button()
        element  = order_feed.element_text(Locators.NUMBER_ORDER)
        personal_account.click_personal_account()
        personal_account.click_order_history()
        element2 = order_feed.element_text(Locators.NUMBER_ORDER)
        assert element == element2

    @allure.title('Проверка при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_counter_for_all_time(self, driver, prepare_user):
        order_burger = BurgerPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account = PersonalAccountPage(driver)
        order_burger.go_to_site_login()
        personal_account.text_field_email(Constants.email)
        personal_account.text_field_password(Constants.password)
        personal_account.click_enter_button()
        sleep(3)
        order_burger.click_order_feed_button()
        element = order_feed.element_text(Locators.COMPLETED_IN_ALL_TIME)
        order_burger.click_constructor_button()
        order_burger.drag_and_drop(Locators.FIRST_INGREDIENT, Locators.CONSTRUCTOR)  # Для FireFox не работает перетягивание
        sleep(2)
        order_burger.click_place_order()
        sleep(3)
        order_burger.click_close()
        order_burger.click_order_feed_button()
        sleep(10)
        element2 = order_feed.element_text(Locators.COMPLETED_IN_ALL_TIME)
        assert element < element2

    @allure.title('Проверка при создании нового заказа счётчик Выполнено за сегодня')
    def test_counter_for_today(self, driver, prepare_user):
        order_burger = BurgerPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account = PersonalAccountPage(driver)
        order_burger.go_to_site_login()
        personal_account.text_field_email(Constants.email)
        personal_account.text_field_password(Constants.password)
        personal_account.click_enter_button()
        sleep(3)
        order_burger.click_order_feed_button()
        element = order_feed.element_text(Locators.COMPLETED_TODAY)
        order_burger.click_constructor_button()
        order_burger.drag_and_drop(Locators.FIRST_INGREDIENT,
                                   Locators.CONSTRUCTOR)  # Для FireFox не работает перетягивание
        sleep(2)
        order_burger.click_place_order()
        sleep(3)
        order_burger.click_close()
        order_burger.click_order_feed_button()
        sleep(10)
        element2 = order_feed.element_text(Locators.COMPLETED_TODAY)
        assert element < element2


    @allure.title('Проверка после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_progress(self, driver, prepare_user):
        order_burger = BurgerPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account = PersonalAccountPage(driver)
        order_burger.go_to_site_login()
        personal_account.text_field_email(Constants.email)
        personal_account.text_field_password(Constants.password)
        personal_account.click_enter_button()
        sleep(3)
        order_burger.drag_and_drop(Locators.FIRST_INGREDIENT,
                                   Locators.CONSTRUCTOR)  # Для FireFox не работает перетягивание
        sleep(2)
        order_burger.click_place_order()
        element = order_feed.element_text(Locators.ORDER_NUMBER_FROM_MAIN_PAGE)
        if isinstance(driver, webdriver.Chrome):
            while True:
                element = order_feed.element_text(Locators.ORDER_NUMBER_FROM_MAIN_PAGE)
                if element != "9999":
                    break
        element = "0"+element
        order_burger.click_close()
        order_burger.click_order_feed_button()
        sleep(3)
        element2= order_feed.element_text(Locators.ORDER_IN_PROGRESS)
        assert element == element2






