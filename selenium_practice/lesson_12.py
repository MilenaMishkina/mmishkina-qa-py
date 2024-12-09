import time

from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Chrome()
driver.get('https://seiyria.com/bootstrap-slider')
time.sleep(1)


EXAMPLE_ONE = ('xpath', '//a[@href="#example-1"]')
SLIDER_LOCATOR = ('xpath', '(//div[@role = "slider"])[1]')

driver.find_element(*EXAMPLE_ONE).click()

def move_slider(slider, target_point, current_position, step):
    if target_point < current_position:
        offset = int((current_position - target_point) / step)
        slider.send_keys(Keys.ARROW_LEFT * offset)
    else:
        offset = int((target_point - current_position) / step)
        slider.send_keys(Keys.ARROW_RIGHT * offset)

def set_range(sldr, target_points, current_point_attr_name, step=1):
    slider = driver.find_element(*sldr)

    current_position = int(slider.get_attribute(current_point_attr_name))

    move_slider(slider, target_points, current_position, step)
    time.sleep(1)

    assert int(slider.get_attribute(current_point_attr_name)) == target_points
    time.sleep(1)


time.sleep(3)
set_range(
    SLIDER_LOCATOR,
    20,
    "aria-valuenow",
    1
)
time.sleep(3)
