from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import variables
from time import sleep
chrome_options = Options()

chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://hirschqa.azurewebsites.net/training/")
driver.find_element(By.ID,"Name").send_keys(variables.name)
sleep(2)
driver.find_element(By.ID,"email").send_keys(variables.email)
sleep(2)
driver.find_element(By.ID,"phone").send_keys(variables.phone)
sleep(2)
driver.find_element(By.ID,"dob").send_keys(variables.dob)
sleep(2)
driver.find_element(By.NAME,"gender").click()
sleep(2)
driver.find_element(By.NAME,"state").send_keys("Tamil Nadu")
sleep(2)
driver.find_element(By.NAME,"institution").send_keys("Thiagarajar College")
sleep(2)
driver.find_element(By.NAME,"percentage[]").send_keys("88.3")
driver.find_element(By.ID,"lang2").click()
driver.find_element(By.CLASS_NAME,"print-button").click()
sleep(3)
print("Test cases are passed")
driver.quit()
