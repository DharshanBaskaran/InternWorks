from selenium.webdriver.remote.webdriver import WebDriver

def scroll_down(driver: WebDriver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scroll_up(driver: WebDriver):
    driver.execute_script("window.scrollTo(0, 0);")

def scroll_to_element(driver: WebDriver, locator):
    element = driver.find_element(*locator)
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element
    )
    return element
