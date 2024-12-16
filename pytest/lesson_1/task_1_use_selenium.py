from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage:
    LOGIN_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    AUTHORIZED_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    INCORRECT_USER_DATA_ALERT = ('xpath', '//div[@role = "alert"]')
    USERNAME_FIELD = ('xpath', '//input[@name = "username"]')
    PASSWORD_FIELD = ('xpath', '//input[@name = "password"]')
    LOGIN_BUTTON = ('xpath', '//button[@type = "submit"]')
    ORANGE_HRM_LINK_BUTTON = ('xpath', '//a[@target = "_blank"][text() = "OrangeHRM, Inc"]')

    USERNAME_DATA = 'Admin'
    INCORRECT_PASSWORD_DATA = 'admin'
    PASSWORD_DATA = 'admin123'
    ORANGE_HRM_LINK = 'https://www.orangehrm.com/'

    def test_authorization_positive(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, timeout=25, poll_frequency=1)

        driver.get(self.LOGIN_URL)
        print(driver.page_source)

        wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD), 'Элемент не найден на странице').send_keys(self.USERNAME_DATA)

        wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD), 'Элемент не найден на странице').send_keys(self.PASSWORD_DATA)

        wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON), 'Элемент не найден на странице').click()

        current_url = driver.current_url

        assert current_url == self.AUTHORIZED_URL, f'URLs are not equal current url is {current_url}'

    def test_authorization_negative(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, timeout=25, poll_frequency=1)

        driver.get(self.LOGIN_URL)

        wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD), 'Элемент не найден на странице').send_keys(self.USERNAME_DATA)

        wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD), 'Элемент не найден на странице').send_keys(self.INCORRECT_PASSWORD_DATA)

        wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON), 'Элемент не найден на странице').click()

        current_url = driver.current_url

        wait.until(EC.visibility_of_element_located(self.INCORRECT_USER_DATA_ALERT), 'Элемент не найден на странице')

        assert current_url == self.LOGIN_URL, f'URLs are not equal current url is {current_url}'

    def test_forgotten_password(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, timeout=25, poll_frequency=1)

        driver.get(self.LOGIN_URL)

        wait.until(EC.visibility_of_element_located(self.ORANGE_HRM_LINK_BUTTON), 'Элемент не найден на странице').click()

        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        current_url = driver.current_url

        assert len(tabs) == 2
        assert current_url == self.ORANGE_HRM_LINK, f'URLs are not equal current url is {current_url}'





