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

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

drag_ele = driver.find_element(By.XPATH, "//div[@id='box6']")
drop_ele = driver.find_element(By.XPATH, "//div[@id='box106']")

action = ActionChains(driver)
action.drag_and_drop(drag_ele, drop_ele).perform()

# Pause to observe result
time.sleep(0.3)

# Optional: Verify the drop was successful
dropped_text = drop_ele.text
print("Drop result:", dropped_text)

time.sleep(1)
driver.quit()
