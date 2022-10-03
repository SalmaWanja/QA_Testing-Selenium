import time

from selenium import webdriver

# Invoked Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/salma.wanja/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice//")

name = "Salma Mbogori"

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

# Switch to java/javascript alerts
alert = driver.switch_to.alert
alertText = alert.text

assert name in alertText

print(alertText)
alert.accept()
#alert.dismiss()
