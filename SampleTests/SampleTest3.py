from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
sleep(5)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
text = driver.find_element(By.CLASS_NAME,"title").text
assert "products" in text.lower()
print("Test Case passed.. Login Successful!!")
#sleep(10)
print("testing add to cart")
add_cart_btns=driver.find_elements(By.CLASS_NAME,"btn_inventory")
for btn in add_cart_btns[:3]:
    btn.click()
print("test case passed!..Added to cart")
sleep(2)
print("remove from cart")
rem_cart_btns=driver.find_elements(By.CLASS_NAME,"btn_inventory")
for btn in rem_cart_btns[:2]:
    btn.click()
print("Test case passed!.. removed from cart")
print("closing..")
driver.close()
