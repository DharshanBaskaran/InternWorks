import logging
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    handlers=[logging.FileHandler('D:\\Github\\InternWorks\\SampleTests\\FormFilling\\logs\\informations.log',mode='a'),
                              logging.StreamHandler()],
)

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
        logging.error("Error while initializing driver!..", driver_exception)
    except Exception as exception:
        logging.error(exception)

