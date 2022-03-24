import time
import math
from selenium import webdriver
from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(
    executable_path='C:/Users/Ruslan/Downloads/chromedriver/chromedriver.exe'
)

try:
    # 1
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    # 2
    element_x = browser.find_element(By.ID, 'input_value')
    x = int(element_x.text)


    # 3
    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))


    # 4
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    #5
    browser.find_element(By.ID, 'answer').send_keys(calc(x))

    #6
    browser.find_element(By.XPATH, '//input[@type="checkbox"]').click()

    #7
    browser.find_element(By.ID, 'robotsRule').click()

    #8
    button.click()

finally:
    time.sleep(30)
    #
