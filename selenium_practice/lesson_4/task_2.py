from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')

username = 'tomsmith'
username_locator = '//input[@id = "username"]'
password = 'SuperSecretPassword!'
password_locator = '//input[@id = "password"]'
login_button_locator = '//button[@type = "submit"]'
logout_button_locator = '//a[contains(@class, "button")]'

username_field = driver.find_element('xpath', username_locator)
username_field.clear()
assert username_field.get_attribute('value') == '', 'Поле заполнено'
username_field.send_keys(username)
assert username in username_field.get_attribute('value'), f'Значениe {username} не найдено в атрибуте "value"'

password_field = driver.find_element('xpath', password_locator)
password_field.clear()
assert password_field.get_attribute('value') == '', 'Поле заполнено'
password_field.send_keys(password)
assert password in password_field.get_attribute('value'), f'Значениe {password} не найдено в атрибуте "value"'

login_button = driver.find_element('xpath', login_button_locator)
login_button.click()

logout_button = driver.find_element('xpath', logout_button_locator)
page_source = driver.page_source
assert login_button not in page_source, 'Элемент найден на странице'