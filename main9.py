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
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")

    #2
    browser.find_element(By.XPATH, "//button[text()='I want to go on a magical journey!']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    #4
    elex = browser.find_element(By.ID, 'input_value')
    x = int(elex.text)

    def calc(x):
        return str(math.log(abs(12*math.sin(x))))

    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    y = alert_text.split(" ")

    print(y[-1])

finally:
    time.sleep(3)
    browser.quit()
    #
