from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, timeout=25, poll_frequency=0)

driver.get('https://omayo.blogspot.com/')

# LOCATORS
disappear_text_after_25_seconds = ('xpath', '//div[@id = "deletesuccess"]')
displayed_text_after_10_seconds = ('xpath', '//div[@id = "delayedText"]')
enabled_button_after_5_seconds = ('xpath', '//input[@id = "timerButton"]')
try_it_button = ('xpath', '//button[contains(@onclick, "setTimeout")][text() = "Try it"]')
disabled_button = ('xpath', '//button[@id = "myBtn"]')

wait.until(EC.invisibility_of_element_located(disappear_text_after_25_seconds), 'Элемент найден на странице')

wait.until(EC.visibility_of_element_located(displayed_text_after_10_seconds), 'Элемент не найден на странице')

wait.until(EC.visibility_of_element_located(enabled_button_after_5_seconds), 'Элемент не найден на странице').is_enabled()

wait.until(EC.visibility_of_element_located(try_it_button)).click()
wait.until(EC.element_attribute_to_include(disabled_button, "disabled"), 'Кнопка в состоянии enabled')