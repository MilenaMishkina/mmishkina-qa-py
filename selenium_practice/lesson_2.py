import time
from selenium import webdriver


driver = webdriver.Chrome()

driver.get('https://testautomationpractice.blogspot.com/')

time.sleep(3)

driver.find_element('class name', 'wikipedia-icon')
driver.find_element('id', 'Wikipedia1_wikipedia-search-input')
driver.find_element('tag name', 'button')