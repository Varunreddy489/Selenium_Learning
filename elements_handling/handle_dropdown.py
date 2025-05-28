import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://www.opencart.com/index.php?route=account/register")

wait = WebDriverWait(driver, 100)
dropdown_element = wait.until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='input-country']"))
)


# select the option from dropdown
dropdown_element.select_by_visible_text("India")
time.sleep(2)
dropdown_element.select_by_value("10")
time.sleep(2)

dropdown_element.select_by_value("13")


driver.quit()
