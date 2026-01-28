from .logger import logger
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options

def get_driver(kiosk_printing=False):
    try:
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if kiosk_printing:
            options.add_argument("--kiosk-printing")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver
    except WebDriverException as driver_exception:
        logger.error("Error while initializing driver!..", driver_exception)
    except Exception as exception:
        logger.error(exception)

