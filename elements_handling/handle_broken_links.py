import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("http://www.deadlinkcity.com/")


links = driver.find_elements(By.XPATH, "//a")
count = 0

for link in links:
    url = link.get_attribute("href")

    try:
        res = requests.head(url)
    except requests.exceptions.RequestException as e:
        None

    if res.status_code > 400:
        print(url, "is a broken link")
        count += 1
    else:
        print(url, "is a valid link")

print(f"Total broken links: {count}")

driver.quit()
