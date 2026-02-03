from .logger import logger
from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver

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
        logger.error("Error while scrolling!",driver_exception)
    except Exception as exception:
        logger.error(exception)

def scroll_up(driver: WebDriver):
    try:
        driver.execute_script("window.scrollTo(0, 0);")
    except WebDriverException as driver_exception:
        logger.error("Error while scrolling up!",driver_exception)
    except Exception as exception:
        logger.error(exception)

def scroll_to_element(driver: WebDriver, locator):
    try:
        element = driver.find_element(*locator)
        driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element
        )
        return element
    except WebDriverException as driver_exception:
        logger.error("Error while scrolling to element!",driver_exception)
    except Exception as exception:
        logger.error(exception)
