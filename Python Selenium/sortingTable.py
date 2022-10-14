from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

service_obj = Service("C:/Users/salma.wanja/PycharmProjects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(10)

browserSortedList = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect veggie names and store in list --> browserSortedList (A, B, C)
vegetableList = driver.find_elements(By.XPATH, "//tr/td[1]")

for veggie in vegetableList:
    browserSortedList.append(veggie.text)

originalVegetableList = browserSortedList.copy()

# Sort the browser --> sort browserSortedList

browserSortedList.sort()

assert browserSortedList == originalVegetableList
