from time import sleep
from locators import FormLocators
from utils import scroll_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, data):
        self.wait.until(EC.visibility_of_element_located(FormLocators.NAME)).send_keys(data.name)
        self.wait.until(EC.visibility_of_element_located(FormLocators.EMAIL)).send_keys(data.email)
        self.wait.until(EC.visibility_of_element_located(FormLocators.PHONE)).send_keys(data.phone)
        self.wait.until(EC.visibility_of_element_located(FormLocators.DOB)).send_keys(data.dob)
        self.wait.until(EC.element_to_be_clickable(FormLocators.GENDER)).click()
        self.wait.until(EC.visibility_of_element_located(FormLocators.STATE)).send_keys(data.state)
        sleep(3)
        scroll_page.scroll_down(self.driver)
        self.wait.until(EC.visibility_of_element_located(FormLocators.INSTITUTION)).send_keys(data.institution)
        self.wait.until(EC.visibility_of_element_located(FormLocators.PERCENTAGE)).send_keys(data.percentage)
        lang_checkbox = scroll_page.scroll_to_element(self.driver, FormLocators.LANGUAGE)
        self.driver.execute_script("arguments[0].click();", lang_checkbox)
        sleep(3)
        print_button = scroll_page.scroll_to_element(self.driver, FormLocators.PRINT_BUTTON)
        self.driver.execute_script("arguments[0].click();", print_button)

