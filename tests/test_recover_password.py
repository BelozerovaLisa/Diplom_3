import allure
import pytest
from time import sleep
from constants import Constants
from locators import Locators
from pages.login_page import LoginPage

@allure.title('Тестируем изменение пароля')
class TestRecoverPassword:
    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_button_recover_password(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site_login()
        login_page.click_forgot_button()
        assert driver.current_url == Constants.URL_FORGOT_PASSWORD

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_edit_password(self,driver):
        login_page = LoginPage(driver)
        login_page.go_to_site_forgot_password()
        login_page.text_field_email(Constants.email)
        login_page.click_recover_button()
        assert driver.current_url == Constants.URL_RESET_PASSWORD

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его»')
    def test_button_show_password(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_site_forgot_password()
        login_page.text_field_email(Constants.email)
        login_page.click_recover_button()
        login_page.text_field_password(Constants.password)
        login_page.click_show_button()
        is_find = login_page.find_element(Locators.PASSWORD_TEXT) # ищем на странице поле с не скрытым паролем
        assert is_find.is_displayed()







