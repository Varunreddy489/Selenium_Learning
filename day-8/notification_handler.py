import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")  # Disable notifications
ops.add_argument("--disable-popup-blocking")  # Disable popup blocking

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj, options=ops)
driver.maximize_window()

driver.get("https://whatmylocation.com/")

time.sleep(5)
driver.quit()