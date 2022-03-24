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
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    #2
    browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys('Ruslan')
    browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys('Mekhtiev')
    browser.find_element(By.XPATH, '//input[@name="email"]').send_keys('`mail@mail.ru')

    #3
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)


    #4
    button = browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]')
    button.click()

finally:
    time.sleep(30)
    #
