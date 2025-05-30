import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com")

# Wait until the Username field is present
wait = WebDriverWait(driver, 10)
username_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
)
username_input.send_keys("Admin")

# Send password
password_input = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password_input.send_keys("admin123")

# Click login button
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()


time.sleep(5)

wait.until(EC.presence_of_element_located((By.LINK_TEXT, "OrangeHRM, Inc")))

# Click external link
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

# Print all window IDs
windows_id = driver.window_handles
print("All Window IDs:", windows_id)


driver.switch_to.window(windows_id[0])
print("Switched to first window:", driver.title)

driver.switch_to.window(windows_id[1])
print("Switched to first window:", driver.title)


time.sleep(2)
driver.quit()
