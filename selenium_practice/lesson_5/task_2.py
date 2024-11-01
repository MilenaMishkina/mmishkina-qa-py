import os
from selenium import webdriver

options = webdriver.ChromeOptions()

preferences = {
    "download.default_directory" : os.path.join(os.getcwd(), "downloads"),
    "safebrowsing.enabled" : True,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
}
options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(options=options)
driver.get('http://the-internet.herokuapp.com/download')

list_of_files = driver.find_elements('xpath', '//a[contains(@href, "download")]')

for element in list_of_files:
    try:
        element.click()
    except FileNotFoundError:
        print('Файл не найден')
