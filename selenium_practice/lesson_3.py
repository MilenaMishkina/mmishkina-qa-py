from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://vk.com/')
VK_TITLE = driver.title
print("Title страницы: ", VK_TITLE)

driver.get('https://ya.ru/')
YANDEX_TITLE = driver.title
print("Title страницы: ", YANDEX_TITLE)

driver.back()
assert VK_TITLE == driver.title, 'Не удалось вернуться на прежнюю страницу'

driver.refresh()
PAGE_URL = driver.current_url
print(PAGE_URL)

driver.forward()
assert PAGE_URL != driver.current_url, 'URL-адрес изменился'