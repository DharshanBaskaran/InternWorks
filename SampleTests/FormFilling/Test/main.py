#import logging
from utils.logger import logger
from selenium.common import WebDriverException

from config import variables
from pages import FormPage
from utils import get_driver


def test_form_submission():
    try:
        driver = get_driver(kiosk_printing=True)
        driver.get("https://hirschqa.azurewebsites.net/training/")
        form_page = FormPage(driver)
        form_page.fill_form(variables)
        logger.info("Test cases are passed")
    except WebDriverException as driver_exception:
        logger.error(driver_exception)
        raise
    except Exception as exception:
        logger.error(exception)
        raise
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    test_form_submission()
