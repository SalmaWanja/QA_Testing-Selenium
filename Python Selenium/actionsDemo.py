from selenium import webdriver
from selenium.webdriver import ActionChains

# Invoked Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C:/Users/salma.wanja/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

actions = ActionChains(driver)

# actions.double_click(driver.find_element(By.ID, "")).perform()
# actions.context_click().perform()

actions.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
