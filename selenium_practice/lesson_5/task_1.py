import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://demoqa.com/upload-download')

upload_file_field = driver.find_element('xpath', '//input[@type ="file"]')
upload_file_field.send_keys(os.path.join(os.getcwd(), "инжинеры.jpg"))
