from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://money.rediff.com/gainers")

child_text_element = driver.find_element(By.XPATH, "//a[contains(text(),'Apollo Micro Systems')]")

text_msg = child_text_element.text
text_link = child_text_element.get_attribute("href")

parent_text_element = driver.find_element(By.XPATH, "//a[contains(text(),'Apollo Micro Systems')]/parent::td").text

ancestor_text_element = driver.find_element(By.XPATH, "//a[contains(text(),'Apollo Micro Systems')]/ancestor::tr").text

childs_count = driver.find_elements(By.XPATH, "//a[contains(text(),'Apollo Micro Systems')]/ancestor::tr/child::td")

descendant_nodes = driver.find_elements(By.XPATH,
                                        "//a[contains(text(),'Apollo Micro Systems')]/ancestor::tr/descendant::*")

# following
following_nodes = driver.find_elements(By.XPATH,
                                       "//a[contains(text(),'Apollo Micro Systems')]/ancestor::tr/following::*")
following_sibling = driver.find_elements(By.XPATH,
                                         "//a[contains(text(),'Apollo Micro Systems')]/ancestor::tr/following-sibling::tr")

# preceding
preceding_nodes = driver.find_elements(By.XPATH,
                                       "//a[contains(text(),'Apollo Micro Systems')]/ancestor::tr/preceding::tr")
preceding_sibling = driver.find_elements(By.XPATH,
                                         "//a[contains(text(),'Apollo Micro Systems')]/ancestor::tr/preceding-sibling::tr")

print("Text:", text_msg)
print("Link:", text_link)
print("Parent:", parent_text_element)
print("Ancestor:", ancestor_text_element)
print("Count of childs:", len(childs_count))

print("Descendats", len(descendant_nodes))

print("Following", len(following_nodes))
print("Following", len(following_sibling))

print("preceding_nodes", len(preceding_nodes))
print("preceding_sibling", len(preceding_sibling))

driver.close()
