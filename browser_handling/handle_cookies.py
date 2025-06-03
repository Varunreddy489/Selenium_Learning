import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up the Chrome driver
service_obj = Service(
    r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
)

driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

cook = driver.get_cookies()
print(len(cook))
# for c in cook:
#     print(c.get("name"),c.get("value"),c.get('expiry'))

# Add new Cookie
driver.add_cookie({"name": "MyCookie", "value": "123123"})

re_cookies = driver.get_cookies()

print(len(re_cookies))

# Delete a Cookie

driver.delete_cookie("MyCookie")
de_cookies = driver.get_cookies()
print("After deleting the cookie:", len(de_cookies))

# Delete All Cookies
driver.delete_all_cookies()
de_cookies = driver.get_cookies()
print("After deleting the cookie:", len(de_cookies))

driver.quit()
