from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="dob"]').click()

datepicker_month = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))
datepicker_month.select_by_visible_text("Dec")

datepicker_year = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
datepicker_year.select_by_visible_text("1990")

alldates  = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in alldates:
    if date.text == '25':
        date.click()
        break