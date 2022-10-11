from selenium import webdriver

# Invoked Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C:/Users/salma.wanja/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").send_keys("My name is Salma Mbogori")

driver.switch_to.default_content()

print(driver.find_element(By.CSS_SELECTOR, "h3").text)