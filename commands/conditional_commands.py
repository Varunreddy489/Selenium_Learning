from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/apparel")

search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

print("Is Enabled:", search_box.is_enabled())
print("Is Displayed:", search_box.is_displayed())

driver.quit()
