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

driver.get("https://practice-automation.com/hover/")

hover_ele = driver.find_element(By.XPATH, "//h3[@id='mouse_over']")

act = ActionChains(driver)
act.move_to_element(hover_ele).perform()

time.sleep(10)
driver.quit()
