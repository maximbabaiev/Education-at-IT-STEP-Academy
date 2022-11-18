import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os.path





driver = webdriver.Chrome(executable_path=r"/08_Module/29_Lesson/chromedriver.exe")


try:
    driver.get(url="https://www.marvel.com/characters")
    comix_url = driver.find_elements(By.CLASS_NAME, "grid-base.grid__6 a")
    with open("characters.txt", "w") as file:
        href_url = []
        for i in comix_url:
            href_url.append(i.get_attribute("href"))
        for el in href_url:
            driver.get(url=el)
            name = driver.find_elements(By.CLASS_NAME, "card-body__headline")
            file.write("Hero: " + name[0].text + "\n")
            info_name = driver.find_elements(By.CLASS_NAME, "railBioInfoItem__label")
            info = driver.find_elements(By.CLASS_NAME, "railBioLinks")
            if info:
                for j in range(len(info)):
                    file.write(info_name[j].text + ": " + info[j].text + "\n")
            else:
                file.write("No information on the Hero")
            file.write("\n\n")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

