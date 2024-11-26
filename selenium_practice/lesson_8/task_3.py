import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=25, poll_frequency=0)

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get('https://www.ozon.ru')
time.sleep(1)

DELETE_BUTTON = ('xpath', '//div[@delete-button-test-id]//button[2]')


# Найти товар
input_field = driver.find_element('xpath', '//input[@name = "text"]')
input_field.clear()
input_field.send_keys('Шкаф')
driver.find_element('xpath', '//button[@aria-label = "Поиск"]').click()
time.sleep(1)

# Добавить в корзину
button_add_to_cart = driver.find_element('xpath', '(//button)[11]')
assert button_add_to_cart.text == 'Завтра'
button_add_to_cart.click()
time.sleep(1)

# Перейти в корзину
driver.find_element('xpath', '//a[@href = "/cart"]').click()

# Сохранить состояние корзины
all_cookies = driver.get_cookies()
pickle.dump(all_cookies, open(os.path.join(os.getcwd(),"cookies", "cookies.pkl"), "wb"))

# Удалить товар из корзины
driver.find_element('xpath', '(//div[@delete-button-test-id]//button)[2]').click()

# Удалить куки
driver.delete_all_cookies()
driver.refresh()
wait.until(EC.invisibility_of_element_located(DELETE_BUTTON), 'Элемент найден на странице')

# Записать куки из файла в переменную
cookies = pickle.load(open(os.path.join(os.getcwd(), "cookies", "cookies.pkl"), "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
assert all_cookies == cookies



