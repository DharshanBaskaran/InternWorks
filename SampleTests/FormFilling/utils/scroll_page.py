import logging
from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    handlers=[logging.FileHandler('D:\\Github\\InternWorks\\SampleTests\\FormFilling\\logs\\informations.log',mode='a'),
                              logging.StreamHandler()],
)

def scroll_down(driver: WebDriver):
    try:
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
    except WebDriverException as driver_exception:
        logging.error("Error while scrolling!",driver_exception)
    except Exception as exception:
        logging.error(exception)

def scroll_up(driver: WebDriver):
    try:
        driver.execute_script("window.scrollTo(0, 0);")
    except WebDriverException as driver_exception:
        logging.error("Error while scrolling up!",driver_exception)
    except Exception as exception:
        logging.error(exception)

def scroll_to_element(driver: WebDriver, locator):
    try:
        element = driver.find_element(*locator)
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element
        )
        return element
    except WebDriverException as driver_exception:
        logging.error("Error while scrolling to element!",driver_exception)
    except Exception as exception:
        logging.error(exception)
