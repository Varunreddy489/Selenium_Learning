import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import excel_utils

serv_obj = Service(r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe")

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=serv_obj, options=chrome_options)
driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 10)

file = "data_driven_testing.xlsx"
rows = excel_utils.get_row_count(file, "Sheet3")

for r in range(2, rows + 1):
    price = excel_utils.read_data(file, "Sheet3", r, 1)
    rate_of_interest = excel_utils.read_data(file, "Sheet3", r, 2)
    per1 = excel_utils.read_data(file, "Sheet3", r, 3)
    per2 = excel_utils.read_data(file, "Sheet3", r, 4)
    fre = excel_utils.read_data(file, "Sheet3", r, 5)
    exp_mvalue = excel_utils.read_data(file, "Sheet3", r, 6)

    driver.find_element(By.ID, "principal").clear()
    driver.find_element(By.ID, "principal").send_keys(price)

    driver.find_element(By.ID, "interest").clear()
    driver.find_element(By.ID, "interest").send_keys(rate_of_interest)

    driver.find_element(By.ID, "tenure").clear()
    driver.find_element(By.ID, "tenure").send_keys(per1)

    Select(driver.find_element(By.ID, "tenurePeriod")).select_by_visible_text(per2)
    Select(driver.find_element(By.ID, "frequency")).select_by_visible_text(fre)

    # Handle overlay popup using WebDriverWait
    try:
        overlay_close = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wzrk-close")))
        overlay_close.click()
    except:
        pass  # Overlay didn't appear

    # Wait for Calculate button and click it
    calc_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img")))
    calc_btn.click()

    # Wait for result to appear
    act_val = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='resp_matval']/strong"))).text

    if float(exp_mvalue) == float(act_val.replace(',', '')):
        print("Pass")
        excel_utils.write_data(file, "Sheet3", r, 8, "Pass")
    else:
        print("Fail")
        excel_utils.write_data(file, "Sheet3", r, 8, "Fail")

time.sleep(3)
driver.quit()
