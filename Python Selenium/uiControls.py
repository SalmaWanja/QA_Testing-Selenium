import time

from selenium import webdriver

# Invoked Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/salma.wanja/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice//")

# This code is to select checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# This code is to select radio buttons

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[2].click() # used instead of for loop when you are sure values are constant

assert radioButtons[2].is_selected()

# for radio in radioButtons:
#     if radio.get_attribute('value') == 'radio2':
#         radio.click()
#         assert radio.is_selected

displaybox = driver.find_element(By.ID, "displayed-text")

assert displaybox.is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not displaybox.is_displayed()




