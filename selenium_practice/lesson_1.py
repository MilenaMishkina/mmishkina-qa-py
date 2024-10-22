import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager(driver_version="112.0.5615.49").install())

with webdriver.Chrome() as driver:
    time.sleep(3)