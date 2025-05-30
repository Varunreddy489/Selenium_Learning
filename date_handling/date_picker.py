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

driver.get("https://jqueryui.com/datepicker/")

# Switch to the iframe containing the datepicker
driver.switch_to.frame(0)

year = "2023"
month = "June"
day = "15"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    month_val = driver.find_element(
        By.XPATH, "//span[@class='ui-datepicker-month']"
    ).text
    year_val = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if month_val == month and year_val == year:
        break
    else:
        # driver.find_element(
        #     By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span"
        # ).click()  # next button to change month
        
        driver.find_element(
            By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span"
        ).click() # previous button to change month
        
dates=find_elements = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in dates:
    if date.text == day:
        date.click()
        break

time.sleep(2)  # Wait for the date to be set
driver.quit()
