from selenium import webdriver

# Invoked Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C:/Users/salma.wanja/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

openedWindows = driver.window_handles

driver.switch_to.window(openedWindows[1])
loginEmail = driver.find_element(By.XPATH, "//a[normalize-space()='mentor@rahulshettyacademy.com']").text
driver.close()

driver.switch_to.window(openedWindows[0])
driver.find_element(By.XPATH, "//input[@id='username']").send_keys(loginEmail)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("12345")
driver.find_element(By.ID, "signInBtn").click()

print(driver.find_element(By.XPATH, "//strong[normalize-space()='Incorrect']").text)

