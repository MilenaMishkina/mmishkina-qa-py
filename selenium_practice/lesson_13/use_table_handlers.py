from selenium import webdriver

from selenium_practice.lesson_13.table_handlers import TableHandler

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
table = TableHandler(driver)

driver.get('https://doka.guide/html/tables/demos/example/')

print(table.get_cell_content(2, 3))
print(table.get_row_content(2))
print(table.get_column_content(4))
print(table.select_film_by_year(2, 4))
print(table.select_film_by_year(3, 4))
