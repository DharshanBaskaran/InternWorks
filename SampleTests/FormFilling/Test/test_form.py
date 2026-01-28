import logging
from selenium.common import WebDriverException
from utils import get_driver
from pages import FormPage
from config import variables

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    handlers=[logging.FileHandler('D:\\Github\\InternWorks\\SampleTests\\FormFilling\\logs\\informations.log',mode='a'),
                              logging.StreamHandler()],
)
def test_form_submission():
    try:
        driver = get_driver(kiosk_printing=True)
        driver.get("https://hirschqa.azurewebsites.net/training/")
        form_page = FormPage(driver)
        form_page.fill_form(variables)
        logging.info("Test cases are passed")
    except WebDriverException as driver_exception:
        logging.error(driver_exception)
    except Exception as exception:
        logging.error(exception)
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    test_form_submission()
