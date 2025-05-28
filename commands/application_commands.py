from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.quit()
