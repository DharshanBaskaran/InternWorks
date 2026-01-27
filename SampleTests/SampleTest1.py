from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://github.com/login")
driver.find_element(By.NAME,"login").send_keys("dharshansb9524@gmail.com")
driver.find_element(By.ID,"password").send_keys("Dharzh@#26")
driver.find_element(By.NAME,"commit").click()
title = driver.title
assert "GitHub" in title
driver.close()