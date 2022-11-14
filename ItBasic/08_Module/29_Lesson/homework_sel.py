import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r'C:\Users\AdminP\PycharmProjects\ItStep\GIT\Education-at-IT-STEP-Academy\ItBasic\08_Module\29_Lesson\chromedriver.exe')

driver.get(url='https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12')

first = driver.find_elements(By.CLASS_NAME, 'meta-title')
second = driver.find_elements(By.CLASS_NAME, 'meta-creators')

with open('file.txt', 'w') as file:
    file.write(f"{str(first.text)} {second.text}")



time.sleep(20)

# elem2 = driver.find_element(By.CLASS_NAME, 'meta-creators')

driver.close()