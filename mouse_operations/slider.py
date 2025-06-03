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

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_val = driver.find_element(By.XPATH, " //*[@id='slider-range']/span[1]")

max_val = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print("Location of sliders before dragging:")
print("Min slider location:", min_val.location)
print("Max slider location:", max_val.location)

action = ActionChains(driver)

# Drag the minimum slider to the right
action.drag_and_drop_by_offset(min_val, 150, 0).perform()
action.drag_and_drop_by_offset(max_val, -150, 0).perform()

# refetch the slider elements to get their new positions
min_val = driver.find_element(By.XPATH, " //*[@id='slider-range']/span[1]")
max_val = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")

print("Location of sliders after dragging:")
print("Min slider location:", min_val.location)
print("Max slider location:", max_val.location)

time.sleep(1)
driver.quit()
