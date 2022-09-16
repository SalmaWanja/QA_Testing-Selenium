# invoke the browser

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Admin/Documents/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# code to autofill sections of a webpage
# ID, NAME, CSSSelectors, XPath, Classname, Linktext

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("salmambogori@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# XPATH -> //tagname[@selector='value']
# CSSSELECTOR -> tagname[selector='value'], #ID, .classname

driver.find_element(By.CSS_SELECTOR ,"input[name='name'").send_keys("Salma Mbogori")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()


driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success!" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello Again")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

driver.close()