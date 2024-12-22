import pytest
import requests
from selenium import webdriver


USERNAME_FIELD = ('xpath', '//input[@name = "username"]')
PASSWORD_FIELD = ('xpath', '//input[@name = "password"]')
USERNAME_DATA = 'Admin'
PASSWORD_DATA = 'admin123'
LOGIN_BUTTON = ('xpath', '//button[@type = "submit"]')

@pytest.fixture(scope="function")
def get_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def get_joke():
    response = requests.get('https://geek-jokes.sameerkumar.website/api')
    joke_text = response.text
    if response.status_code == 200:
        return joke_text
    else:
        print('Ошибка при загрузке страницы')

@pytest.fixture
def setup_method(get_driver):
    get_driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    get_driver.find_element(*USERNAME_FIELD).send_keys(USERNAME_DATA)
    get_driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD_DATA)
    get_driver.find_element(*LOGIN_BUTTON).click()
    return
