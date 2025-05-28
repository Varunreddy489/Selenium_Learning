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

# Open the webpage
driver.get("https://testautomationpractice.blogspot.com/")

# Select a single checkbox
driver.find_element(By.XPATH, "//input[@id='sunday']").click()

# Select multiple checkboxes
checkboxes = driver.find_elements(
    By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]"
)
# for checkbox in checkboxes:
#     checkbox.click()

# select checkboxes on choice
for checkbox in checkboxes:

    weekname = checkbox.get_attribute("id")
    if weekname in ["sunday", "monday", "tuesday"]:
        checkbox.click()

time.sleep(2)
driver.quit()
