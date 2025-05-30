import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

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

# naviagate to the admin page
admin_menu = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))
)
admin_menu.click()

# rows = driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr")

rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div[@role='row']")

print(f"Total number of rows: {len(rows)}")
for r in rows:
    status = driver.find_element(
        By.XPATH, "//table[@id='resultTable']/tbody/tr[" + str(r) + "]/td[5]"
    ).text


time.sleep(5)

driver.quit()
