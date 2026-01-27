from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
print("Testing Started!!!")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
sleep(5)
title = driver.title
assert title == "Swag Labs"
print("Testing Successfull and Completed!!!")
driver.quit()
