import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Varunreddy")
driver.find_elements(By.CSS_SELECTOR,"input.inputtext")[1].send_keys("Varun")

time.sleep(10)