import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://amazon.com")
driver.get("https://www.ajio.com/")

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()

driver.quit()
