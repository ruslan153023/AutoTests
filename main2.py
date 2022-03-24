import time
import math
from selenium import webdriver
from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome(
        executable_path='C:\\Users\\Ruslan\\Downloads\\chromedriver\\chromedriver.exe'
    )
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    element_x = browser.find_element(By.ID, "num1")
    x = int(element_x.text)

    element_y = browser.find_element(By.ID, "num2")
    y = int(element_y.text)

    z = str(y + x)

    Select(browser.find_element(By.XPATH, "//select[@id='dropdown']")).select_by_value(z)

    browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    time.sleep(30)
#