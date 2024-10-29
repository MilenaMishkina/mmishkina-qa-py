from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://demoqa.com/text-box')

name = 'Milena'
email = 'mishkina1002@mail.ru'
current_address = 'Testovskaya street, 123'
permanent_address = 'Testovskaya street, 456'

username_field = driver.find_element('xpath', '//input[@id = "userName"]')
username_field.clear()
assert username_field.get_attribute('value') == ''
username_field.send_keys(name)
assert name in username_field.get_attribute('value')

email_field = driver.find_element('xpath', '//input[@id = "userEmail"]')
email_field.clear()
assert email_field.get_attribute('value') == ''
email_field.send_keys(email)
assert email in email_field.get_attribute('value')


current_address_field = driver.find_element('xpath', '//textarea[@id = "currentAddress"]')
current_address_field.clear()
assert current_address_field.get_attribute('value') == ''
current_address_field.send_keys(current_address)
assert current_address in current_address_field.get_attribute('value')


permanent_address_field = driver.find_element('xpath', '//textarea[@id = "permanentAddress"]')
permanent_address_field.clear()
assert permanent_address_field.get_attribute('value') == ''
permanent_address_field.send_keys(permanent_address)
assert permanent_address in permanent_address_field.get_attribute('value')


