import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//input[@id='singleFileInput']").send_keys(
    r"C:\Users\varun\OneDrive\Desktop\Screenshot (82).png")

time.sleep(5)
driver.quit()
