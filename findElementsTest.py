import time

from selenium import webdriver

# Invoked Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/salma.wanja/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)

# Use .elements not .element : plural will search the whole page
# singular will search from top left
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a ")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == 'India'

