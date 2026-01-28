from time import sleep

from utils import get_driver
from pages import FormPage
from config import variables

def test_form_submission():

    driver = get_driver(kiosk_printing=True)
    driver.get("https://hirschqa.azurewebsites.net/training/")
    form_page = FormPage(driver)
    form_page.fill_form(variables)
    print("Test case passed")
    driver.quit()

if __name__ == "__main__":
    test_form_submission()
