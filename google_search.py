import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://www.google.com")


# Wait for search input and enter query
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "gLFyf")))
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("Selenium" + Keys.ENTER)

# Wait for and click on a Selenium link
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Selenium"))
)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium")
link.click()

time.sleep(200)
driver.quit()
