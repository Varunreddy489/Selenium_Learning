from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/login")

email = driver.find_element(By.XPATH, "//input[@id='Email']")

email.clear()

email.send_keys("Varunreddy@gmail.com")

print("Email Value:", email.text)
print("Email get attribute:", email.get_attribute('value'))

driver.quit()
