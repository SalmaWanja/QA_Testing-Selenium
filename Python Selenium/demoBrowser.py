# This code is to test whether a browser opens
from selenium import webdriver

# chrome cannot be invoked alone
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/Admin/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://courses.rahulshettyacademy.com/courses")
driver.back()
driver.refresh()
driver.forward()
driver.minimize_window()
driver.close()

#to make tests for the other browsers, just change the webdriver to the specific browser desired.
#everything else remains the same