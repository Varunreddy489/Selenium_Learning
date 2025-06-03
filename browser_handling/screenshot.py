import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
location = os.getcwd()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

time.sleep(5)

driver.save_screenshot(os.path.join(location, "screenshot.png"))

driver.quit()
