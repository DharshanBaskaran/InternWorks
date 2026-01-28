from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(kiosk_printing=False):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    if kiosk_printing:
        options.add_argument("--kiosk-printing")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver
