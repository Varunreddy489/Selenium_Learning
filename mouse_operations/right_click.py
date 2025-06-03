import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://vinothqaacademy.com/mouse-event/")

right_click_btn = driver.find_element(By.XPATH, "//button[@id='rightclick']")

act = ActionChains(driver)
act.context_click(right_click_btn).perform()

time.sleep(1)
driver.quit()
