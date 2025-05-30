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

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("//iframe[@name='googlefcPresent']")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame("//iframe[@name='googlefcPresent']")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()


driver.switch_to.frame("//iframe[@name='googlefcPresent']")
driver.find_element(By.XPATH, "//a[normalize-space()='Help']").click()
driver.switch_to.default_content()


driver.quit()
