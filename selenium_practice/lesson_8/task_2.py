from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.freeconferencecall.com')

print(driver.get_cookie('test_AB_site_tag'))

driver.delete_cookie('test_AB_site_tag')
driver.refresh()

print(driver.get_cookie('test_AB_site_tag'))

