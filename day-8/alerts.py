import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Prompt']"
).click()


alert_window = driver.switch_to.alert

print(alert_window.text)
alert_window.send_keys("Hello, this is a test message!")

alert_window.accept()
alert_window.dismiss()

time.sleep(2)

driver.quit()
