import allure
import requests

from constants import Constants

class API_Endpoints:
    host = Constants.URL_MAIN
    @allure.step('Создаем пользователя')
    def create_user(self, data):
        url = f'{self.host}/api/auth/register'
        response = requests.post(url, data=data)
        return response

    @allure.step('Логируем  пользователя')
    def login_user(self, data):
        url = f'{self.host}/api/auth/login'
        response = requests.post(url, data=data)
        return response

    @allure.step('Удаляем пользователя')
    def delete_user(self, token):
        url = f'{self.host}/api/auth/user'
        response = requests.delete(url, headers={'Authorization': token})
        return response