from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)



year = '2025'
month = 'December'
date = '02'
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
wait = WebDriverWait(driver, 10)


while True:
     m = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
     y = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
     if m == month and y == year:
         break
     else :
         next_arrow = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[2]')
         next_arrow.click()

         # prev_arrow =  driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/a[1]')
         # prev_arrow.click()
         # wait.until(EC.staleness_of(driver.find_element(By.CLASS_NAME, "ui-datepicker-month")))
         # time.sleep(0.5)

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text == date:
        try:
            ele.click()
        except Exception as e:
            print("Error while clicking date:", e)
        time.sleep(2)
        break

time.sleep(5)
driver.close()