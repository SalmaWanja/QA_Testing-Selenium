from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors--")

service_obj = Service("C:/Users/salma.wanja/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice//")

# Javascript code to scroll down a page
driver.execute_script("window.scrollBy(0,500);")

# Code to screenshot finding
driver.get_screenshot_as_file("screenshot.png")