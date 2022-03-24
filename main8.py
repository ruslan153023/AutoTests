import time
import math
from selenium import webdriver
from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

browser = webdriver.Chrome(
    executable_path='C:/Users/Ruslan/Downloads/chromedriver/chromedriver.exe'
)

try:
    #1
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    #2
    browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']").click()

    #3
    confirm = browser.switch_to.alert
    confirm.accept()

    #4
    elex = browser.find_element(By.ID, 'input_value')
    x = int(elex.text)

    def calc(x):
        return str(math.log(abs(12*math.sin(x))))

    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()

    print(alert_text.split(" "))

finally:
    time.sleep(3)
    browser.quit()
    #
