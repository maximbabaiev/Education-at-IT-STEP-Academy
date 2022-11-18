import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os.path

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

driver = webdriver.Chrome(executable_path=r"/08_Module/29_Lesson/chromedriver.exe")
driver.get(url='https://www.marvel.com/comics?&options%5Boffset%5D=0&totalcount=12')

comix_url = driver.find_elements(By.CLASS_NAME, "row-item-text")
str_var = ''
for i in comix_url:
    var = i.text.split('\n')
    if len(var) > 1:
        pass
    else:
        str_var = str_var + f"{var[0]}\n"
        print(str_var)


path = os.path.join('data', 'not_author.txt')
file = open(path,'w')
file.write(str_var)
file.close()
driver.close()