import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os.path


driver = webdriver.Chrome(executable_path=r"/08_Module/29_Lesson/chromedriver.exe")

driver.get(url='https://www.marvel.com/')
# driver.save_screenshot('scr.png')
# driver.refresh()
# title = driver.title
# print(title)
ls = []
elem = driver.find_elements(By.CLASS_NAME, 'card-body__headline')
for i in elem:
    print(i.text)

time.sleep(20)

driver.close()


