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

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# 1 Scroll down page by pixel

# driver.execute_script("window.scrollBy(0, 3000)")
#
# y_offset=driver.execute_script("return window.pageYOffset")
# print("Current Y Offset:", y_offset)


# 2 Scroll down page till element

flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();", flag)
value = driver.execute_script("return window.pageYOffset")
print("Current Y Offset after scrolling to India flag:", value)

# 3. Scroll down page till end
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# value = driver.execute_script("return window.pageYOffset")
# print("Current Y Offset after scrolling to India flag:", value)

time.sleep(1)
driver.quit()
