import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://text-compare.com/")

textarea_1 = driver.find_element(By.XPATH, '//*[@id="inputText1"]')
textarea_2 = driver.find_element(By.XPATH, '//*[@id="inputText2"]')

textarea_1.send_keys("Hello, this is a test message.")
act = ActionChains(driver)

# select all text in the first textarea
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# copy the selected text
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#switch to the second textarea
act.send_keys(Keys.TAB).perform()

# paste the copied text into the second textarea_2

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

# click on the compare button

driver.find_element(By.XPATH, "//div[@class='compareButtonText']").click()

time.sleep(10)
driver.quit()
