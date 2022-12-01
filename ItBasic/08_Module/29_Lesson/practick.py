import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import os.path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from easygui import *

# Task 1
# driver = webdriver.Chrome(executable_path=r"/08_Module/29_Lesson/chromedriver.exe")
# driver.get(url='https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12')
# list_1 = []
# comix_url = driver.find_elements(By.CLASS_NAME, "meta-title")
# for el in comix_url:
#     list_1.append(el.get_attribute("href"))
# # print(list_1)
# for el in range(len(list_1)):
#     driver.get(list_1[el])
#     driver.save_screenshot(f"scr/{el}.png")
#
#
# driver.close()


# Task 2

# driver = webdriver.Chrome(executable_path=r"/08_Module/29_Lesson/chromedriver.exe")
# driver.get(url='https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12')
# list_url = []
# list_name = []
# comix_url = driver.find_elements(By.CLASS_NAME, "meta-title")
# for el in comix_url:
#     list_url.append(el.get_attribute("href"))
#     list_name.append(el.text)
# for i in range(len(list_url)):
#     if "captain america" in list_name[i].lower():
#         driver.get(list_url[i])
#         driver.save_screenshot(f"scr/{i}.png")
#
#
# driver.close()

# Task 3

# driver = webdriver.Chrome(executable_path=r"/08_Module/29_Lesson/chromedriver.exe")
# driver.get(url='https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12')
#
# comix_url = driver.find_elements(By.CLASS_NAME, "row-item-text")
# str_var = ''
# for i in comix_url:
#     var = i.text.split('\n')
#     if len(var) > 1:
#         pass
#     else:
#         str_var = str_var + f"{var[0]}\n"
#         print(str_var)
#
#
# path = os.path.join('data', 'not_author.txt')
# file = open(path,'w')
# file.write(str_var)
# file.close()
# driver.close()


# Task 4

# driver = webdriver.Chrome(executable_path=r"/08_Module/29_Lesson/chromedriver.exe")
# driver.get(url='https://www.microsoft.com/uk-ua/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook')
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mectrl_headerPicture")))
# driver.find_element(By.ID, 'mectrl_headerPicture').click()
# WebDriverWait(driver, 5).until(EC.presence_of_element_located(
#     (By.ID, "i0116")))
# driver.find_element(By.ID, "i0116").send_keys('pwer666777@outlook.com')
# driver.find_element(By.ID, "idSIButton9").click()
# time.sleep(1)
# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'i0118')))
# driver.find_element(By.ID, 'i0118').send_keys('Maksuwa1')
# driver.find_element(By.ID, 'idSIButton9').click()
# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "idBtn_Back")))
# driver.find_element(By.ID, 'idBtn_Back').click()
# WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.ID, 'id__9')))
# driver.find_element(By.ID, 'id__9').click()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
#                                                                 "#docking_InitVisiblePart_0 > div > div.QFieH > div:nth-child(1) > div > div.AtODR.lG_qQ > div > div > div.VbY1P.T6Va1.Z4n09")))
# driver.find_element(By.CSS_SELECTOR,
#                     "#docking_InitVisiblePart_0 > div > div.QFieH > div:nth-child(1) > div > div.AtODR.lG_qQ > div > div > div.VbY1P.T6Va1.Z4n09").send_keys(
#     "sasha.ozerov98@gmail.com")
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#sug-footer-item2 > div > div")))
# driver.find_element(By.CSS_SELECTOR, "#sug-footer-item2 > div > div").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, '#editorParent_1 > div').send_keys("Привет от Бабаева Максима")
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
#                                                             '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[3]/div[1]/div/div/span/button[1]')))
# driver.find_element(By.XPATH,
#                     '//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[3]/div[1]/div/div/span/button[1]').click()
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ok-1")))
# driver.find_element(By.ID, "ok-1").click()
# time.sleep(10)
# driver.close()
# driver.quit()

# Task 5



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
            # button_price = buttonbox("Что хотите сделать", "Цена", ["Узнать цену и тип груза"])
            # if button_price == "Узнать цену и тип груза":
            #     wait.until(EC.presence_of_all_elements_located(
            #         (By.XPATH, '//*[@id="search-results"]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[4]')))
            #     result_price = driver.find_elements(By.XPATH,
            #                                         '//*[@id="search-results"]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[4]')
            #     for i in result_price:
            #         print(i.text)
        elif button == "Отмена":
            break
        else:
            break
except Exception as ex:
    print(ex)

finally:
    driver.close()
