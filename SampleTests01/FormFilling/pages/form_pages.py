from utils.logger import logger
from time import sleep
from selenium.common import WebDriverException
from locators import FormLocators
from utils import scroll_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, data):
        try:
            self.wait.until(EC.visibility_of_element_located(FormLocators.NAME)).send_keys(data.name)
            self.wait.until(EC.visibility_of_element_located(FormLocators.EMAIL)).send_keys(data.email)
            self.wait.until(EC.visibility_of_element_located(FormLocators.PHONE)).send_keys(data.phone)
            self.wait.until(EC.visibility_of_element_located(FormLocators.DOB)).send_keys(data.dob)
            self.wait.until(EC.element_to_be_clickable(FormLocators.GENDER)).click()
            self.wait.until(EC.visibility_of_element_located(FormLocators.STATE)).send_keys(data.state)
            sleep(3)
            scroll_page.scroll_down(self.driver)
            rows = self.driver.find_elements(
                By.XPATH, "//table//tbody//tr"
            )
            degree_row = rows[0]
            degree_inputs = degree_row.find_elements(By.TAG_NAME, "input")

            degree_inputs[0].send_keys(data.degree_institution)
            degree_inputs[1].send_keys(data.degree_percentage)

            hs_row = rows[1]
            hs_inputs = hs_row.find_elements(By.TAG_NAME, "input")

            hs_inputs[0].send_keys(data.hs_institution)
            hs_inputs[1].send_keys(data.hs_percentage)
            lang_checkbox = scroll_page.scroll_to_element(self.driver, FormLocators.LANGUAGE)
            self.driver.execute_script("arguments[0].click();", lang_checkbox)
            sleep(3)
            actions = ActionChains(self.driver)

            hirsch_image = self.driver.find_element(
                By.XPATH, "//img[contains(@src,'hirsch')]"
            )

            actions.move_to_element(hirsch_image).perform()
            sleep(3)

            parent_link = hirsch_image.find_element(By.XPATH, "./parent::a")
            pdf_url = parent_link.get_attribute("href")

            logger.info(f"PDF URL: {pdf_url}")

            main_window = self.driver.current_window_handle
            parent_link.click()

            for handle in self.driver.window_handles:
                if handle != main_window:
                    self.driver.switch_to.window(handle)
                    break
            sleep(5)
            self.driver.close()

            self.driver.switch_to.window(main_window)
            print_button = scroll_page.scroll_to_element(self.driver, FormLocators.PRINT_BUTTON)
            self.driver.execute_script("arguments[0].click();", print_button)
        except WebDriverException as driver_exception:
            logger.error(driver_exception)
            raise
        except Exception as exception:
            logger.error(exception)
            raise

