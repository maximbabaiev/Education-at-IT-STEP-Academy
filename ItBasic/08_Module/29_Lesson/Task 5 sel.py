import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from easygui import *

try:
    service = Service(
        r"C:\Users\AdminP\PycharmProjects\ItStep\GIT\Education-at-IT-STEP-Academy\ItBasic\08_Module\29_Lesson\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    wait = WebDriverWait(driver, 10)
    driver.get(url="https://lardi-trans.ua/ru/gruz/")
    wait.until(EC.presence_of_element_located((By.ID, 'react-select-4-input')))
    where_city = driver.find_element(By.ID, 'react-select-4-input')
    while True:
        button = buttonbox("Что хотите сделать", "Грузы", ["Взять", "Отмена"])
        if button == "Взять":
            choice = enterbox("Укажите город загрузки")
            where_city.send_keys(f"{choice}")
            time.sleep(1)
            where_city.send_keys(Keys.ENTER)
            wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="proposal-search"]/div/div/div[3]/div[2]/button')))
            driver.find_element(By.XPATH, '//*[@id="proposal-search"]/div/div/div[3]/div[2]/button').click()
            wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="search-results"]/div/div[1]/div[3]')))
            result = driver.find_elements(By.XPATH, '//*[@id="search-results"]/div/div[1]/div[3]')
            for el in result:
                print(el.text)
            time.sleep(2)
            wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, '//*[@id="search-results"]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[4]')))
            result_price = driver.find_elements(By.XPATH,
                                                '//*[@id="search-results"]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[4]')
            for i in result_price:
                print(i.text)
        elif button == "Отмена":
            break
        else:
            break
except Exception as ex:
    print(ex)

finally:
    driver.close()
