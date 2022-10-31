# n = input("enter miles: ")
# mile = 1.609
# km = float(n) * mile
# if km > 70:
#      print("Збавь скорость!")
import math
# kg = 1000
# gram = float()
import random

login = input("Login: ")
password = ""
for i in range(5):
    password = password + random.choice(list("1234567890abcAB"))
print(login, password)




