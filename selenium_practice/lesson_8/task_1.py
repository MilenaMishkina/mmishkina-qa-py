from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://tilda.cc/login/')

driver.add_cookie({
    'name': 'username',
    'value': 'name123'
})

print(driver.get_cookie('username'))
