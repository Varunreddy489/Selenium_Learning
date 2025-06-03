import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj, options=ops)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

reg_link = Keys.CONTROL + Keys.RETURN
driver.find_element(By.LINK_TEXT, "Register").send_keys(reg_link)

# Open a new tab and switch to it

driver.get("https://www.opencart.com/")
driver.switch_to.new_window('tab')
driver.get("https://orangehrmlive.com/")

# Open a new browser and switch to new window

# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('window')
# driver.get("https://orangehrmlive.com/")

time.sleep(5)
driver.quit()
