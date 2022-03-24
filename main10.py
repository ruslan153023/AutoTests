import time
import math
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome(
    executable_path='C:/Users/Ruslan/Downloads/chromedriver/chromedriver.exe'
)

try:
    #1
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #2

    button = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 3
    browser.find_element(By.ID, "book").click()

    # 4
    elex = browser.find_element(By.ID, 'input_value')
    x = int(elex.text)

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))


    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()

    print(alert_text.split(" "))


finally:
    time.sleep(3)
    browser.quit()
    #

'''
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
'''