from selenium.webdriver.common.by import By

class FormLocators:
    NAME = (By.ID, "Name")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    DOB = (By.ID, "dob")
    GENDER = (By.NAME, "gender")
    STATE = (By.NAME, "state")
    INSTITUTION = (By.NAME, "institution")
    PERCENTAGE = (By.NAME, "percentage[]")
    LANGUAGE = (By.ID, "lang2")
    PRINT_BUTTON = (By.CLASS_NAME, "print-button")