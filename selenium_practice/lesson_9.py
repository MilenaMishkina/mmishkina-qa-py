import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://demoqa.com/selectable')

GRID_BUTTON = ('xpath', '//a[@id = "demo-tab-grid"]')

driver.find_element(*GRID_BUTTON).click()

list_of_checkboxes = driver.find_elements('xpath', '//li[@class = "list-group-item list-group-item-action"]')

# Select elements and check active
for element in list_of_checkboxes[:3]:
    element.click()
    assert 'active' in element.get_attribute('class'), 'Чекбокс не выбран'
    time.sleep(2)

# Select elements and check inactive
for element in list_of_checkboxes[:3]:
    element.click()
    assert 'active' not in element.get_attribute('class'), 'Чекбокс выбран'
    time.sleep(2)


