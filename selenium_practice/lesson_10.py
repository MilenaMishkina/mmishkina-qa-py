import time

from selenium import webdriver
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

OZON_URL = 'https://www.ozon.ru'
CART_BUTTON = ('xpath', '//a[@href = "/cart"]')
CART_OZON_LINK = 'https://www.ozon.ru/cart'
AVITO_URL = 'https://www.avito.ru/'
FOR_BUSINESS_BUTTON = ('xpath', '//a[@href = "/business"]')
FOR_BUSINESS_LINK = 'https://www.avito.ru/business'
HYPER_SKILL_LINK = 'https://hyperskill.org/login'
START_FOR_FREE_BUTTON = ("xpath", "//button//span[normalize-space()='Start for free']")
REGISTER_LINK = 'https://hyperskill.org/register'

driver.get(OZON_URL)
time.sleep(1)
driver.switch_to.new_window('tab')
driver.switch_to.new_window('tab')

tabs = driver.window_handles
assert len(tabs) == 3, 'Количество вкладок не равно 3'

driver.switch_to.window(tabs[0])
time.sleep(1)

assert OZON_URL in driver.current_url, f'Открытая другая вкладка: {driver.current_url}'

page_title = driver.title
print("Title страницы: ", page_title)

driver.find_element(*CART_BUTTON).click()
tabs = driver.window_handles
driver.switch_to.window(tabs[3])
time.sleep(1)
assert CART_OZON_LINK == driver.current_url, f'Адрес текущей страницы {driver.current_url}'

driver.switch_to.window(tabs[1])
driver.get(AVITO_URL)

time.sleep(1)

assert AVITO_URL == driver.current_url, f'Открытая другая вкладка: {driver.current_url}'

page_title = driver.title
print("Title страницы: ", page_title)

driver.find_element(*FOR_BUSINESS_BUTTON).click()
time.sleep(2)
assert FOR_BUSINESS_LINK == driver.current_url, f'Адрес текущей страницы {driver.current_url}'

driver.switch_to.window(tabs[2])
driver.get(HYPER_SKILL_LINK)

time.sleep(1)

assert HYPER_SKILL_LINK == driver.current_url, f'Открытая другая вкладка: {driver.current_url}'

page_title = driver.title
print("Title страницы: ", page_title)

driver.find_element(*START_FOR_FREE_BUTTON).click()
time.sleep(2)
assert REGISTER_LINK == driver.current_url, f'Адрес текущей страницы {driver.current_url}'