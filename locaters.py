from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

inputs = driver.find_elements(By.TAG_NAME,'input')
print(len(inputs))