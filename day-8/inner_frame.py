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

driver.get("https://demo.automationtesting.in/Frames.html")


driver.find_element(
    By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']"
).click()

outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")

driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Hello World")

# Switch back to the parent frame
driver.switch_to.parent_frame()

time.sleep(2)
driver.quit()
