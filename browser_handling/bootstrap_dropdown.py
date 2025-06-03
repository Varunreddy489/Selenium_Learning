import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj, options=ops)
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

countries_list = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")

print(len(countries_list))

for country in countries_list:

    if country == "India":
        country.click()
        break

time.sleep(5)
driver.quit()
