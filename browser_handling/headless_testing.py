from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def chrome_setup():
    service_obj = ChromeService(
        r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe")

    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")

    chrome_driver = webdriver.Chrome(service=service_obj, options=ops)
    return chrome_driver


def edge_setup():
    service_obj = EdgeService(
        r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\msedgedriver.exe"
    )

    ops = webdriver.EdgeOptions()
    ops.add_argument("--headless")

    edge_driver = webdriver.Edge(service=service_obj, options=ops)
    return edge_driver


def firefox_setup():
    service_obj = FirefoxService(
        r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\geckodriver.exe"
    )

    ops = webdriver.FirefoxOptions()
    ops.add_argument("--headless")

    firefox_driver = webdriver.Firefox(service=service_obj, options=ops)
    return firefox_driver


# driver = chrome_setup()
# driver = firefox_setup()
driver = edge_setup()

driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.quit()
