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

driver.get("https://testautomationpractice.blogspot.com/")

# 1. Count No.of rows and cols in the table
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")

cols = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")

print(f"Number of rows: {len(rows)}")
print(f"Number of columns: {len(cols)}")

# 2. Read Specific row Data
row_data = driver.find_element(
    By.XPATH, "//table[@name='BookTable']/tbody/tr[3]/td[2]"
).text

print(f"Data in row 3, column 2: {row_data}")

# 3 Read All Data in the table
all_data = driver.find_elements(By.XPATH, "//table[@name='BookTable']//td")

print(all_data)
for data in all_data:
    print(data.text)

# 4. Read data on condition
for r in range(2, len(rows) + 1):
    author_name = driver.find_element(
        By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]"
    ).text
    if author_name == "Mukesh":
        book_name = driver.find_element(
            By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]"
        ).text
        subject_name = driver.find_element(
            By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[3]"
        ).text
        price = driver.find_element(
            By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]"
        ).text

        print(f"Book by Mukesh: {book_name}")
        print(f"Book Subject: {subject_name}")
        print(f"Price of Book : {price}")

driver.quit()
