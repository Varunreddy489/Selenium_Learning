import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")


# driver.find_element(By.LINK_TEXT, "Digital downloads").click()


# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

links = driver.find_elements(By.XPATH, "//a")
print(f"Total links: {len(links)}")

for link in links:
    print(link.text)
    

driver.quit()
