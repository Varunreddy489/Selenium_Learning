import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/apparel")

# Locator with single element matching
element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

# Locator with multiple element matching
mul_element = driver.find_elements(By.XPATH, "//div[@class='footer']//a")

for ele in mul_element:
    print(ele)

time.sleep(4)

driver.quit()
