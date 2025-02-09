import allure
import pytest
from time import sleep

from constants import Constants
from locators import Locators
from pages.personal_account_page import PersonalAccountPage

@allure.title('Тестируем личный кабинет')
class TestPersonalAccount:
    @allure.title('Проверка перехода по кнопке "Личный кабинет"')
    def test_button_personal_account(self, driver):
        personal_account = PersonalAccountPage(driver)
        personal_account.go_to_site_main()
        personal_account.click_personal_account()
        assert driver.current_url == Constants.URL_LOGIN

    @allure.title('Проверка перехода в раздел История заказов"')
    def test_button_order_history(self, driver, prepare_user):
        personal_account = PersonalAccountPage(driver)
        personal_account.go_to_site_login()
        personal_account.text_field_email(Constants.email)
        personal_account.text_field_password(Constants.password)
        personal_account.click_enter_button()
        personal_account.click_personal_account()
        personal_account.click_order_history()
        assert driver.current_url == Constants.URL_ORDER_HISTORY

    @allure.title('Проверка выход из аккаунтa"')
    def test_button_exit(self, driver, prepare_user):
        personal_account = PersonalAccountPage(driver)
        personal_account.go_to_site_login()
        personal_account.text_field_email(Constants.email)
        personal_account.text_field_password(Constants.password)
        personal_account.click_enter_button()
        personal_account.click_personal_account()
        personal_account.log_out()
        assert driver.current_url == Constants.URL_LOGIN