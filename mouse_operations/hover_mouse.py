import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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

admin_menu = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-main-menu-item active']"))
)
admin_menu.click()

admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']")

userMgmt = driver.find_element(By.XPATH, "//*[@id='userManagement']")

users = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSysemUsers']")

act = ActionChains(driver)
act.move_to_element(admin).move_to_element(userMgmt).move_to_element(users).click().perform()

time.sleep(10)
driver.quit()

# admin_menu = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//a[@class='oxd-main-menu-item active']"))
# )
# admin_menu.click()
