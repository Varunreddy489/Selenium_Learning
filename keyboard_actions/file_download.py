import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def chrome_setup():
    download_path = os.getcwd()

    preferences = {
        "download.default_directory": download_path,
    }

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", preferences)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    service_obj = ChromeService(
        r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\chromedriver.exe"
    )

    return webdriver.Chrome(service=service_obj, options=options)


def edge_setup():
    download_path = os.getcwd()

    preferences = {
        "download.default_directory": download_path,
    }

    options = webdriver.EdgeOptions()
    options.add_experimental_option("prefs", preferences)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    service_obj = EdgeService(
        r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\msedgedriver.exe"
    )

    return webdriver.Edge(service=service_obj, options=options)


def firefox_setup():
    download_path = r"C:\Users\varun\OneDrive\Desktop"

    service_obj = FirefoxService(
        r"C:\Users\varun\OneDrive\Desktop\GE\BROWSER DRIVERS\geckodriver.exe"
    )
    ops = webdriver.FirefoxOptions()

    # 0-default, 1-desktop, 2-custom
    ops.set_preference("browser.download.folderList", 2)
    ops.set_preference("browser.download.dir", download_path)
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.helper.neverAsk.saveToDisk", "application/pdf")
    ops.set_preference("pdfjs.disabled", True)
    return webdriver.Firefox(service=service_obj, options=ops)


# Choose one browser setup
# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()

driver.get("https://www.filesampleshub.com/format/document/pdf")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//li[1]//a[1]").click()

print("Download started...")
time.sleep(50)
driver.quit()
