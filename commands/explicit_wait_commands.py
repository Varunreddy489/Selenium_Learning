from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/login")

wait = WebDriverWait(driver, 10)
email = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='Email']")))

email.clear()
email.send_keys("Varunreddy@gmail.com")

driver.quit()
