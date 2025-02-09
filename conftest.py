import pytest
from selenium import webdriver

from api_user import API_Endpoints
from constants import Constants
api = API_Endpoints()

@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    if request.param == "firefox":
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    else:
        raise ValueError('Unknown browser type')
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture()
def prepare_user():
    user = api.create_user(Constants.USER_DATA)
    login = api.login_user(Constants.USER_DATA)
    yield (user, login)
    api.delete_user(login.json()['accessToken'])
