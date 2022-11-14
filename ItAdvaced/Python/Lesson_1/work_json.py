import json
import os.path

# task 1

# path = os.path.join("data_base", "test1.json")
#
# dict_var = {
#     1: "Nosachenko",
#     "Max": "Babaiev",
#     "Saha": "Ozerov"
# }
#
# with open(path, "w") as oleg:
#     json.dump(dict_var, oleg)  # dump- для сереализации данных(загрузка)
#
#
# with open(path, "r") as max:
#     dict_var = json.load(max)  # load- для десереализации данных(выгрузка)
# print(dict_var)

# task 2

# path = os.path.join("data_base", "test2.json")
#
# list_var = [int(i) for i in input().split()]
#
# with open(path, "w") as list1:
#     json.dump(list_var, list1)

# task 3

path = os.path.join("data_base", "test1.json")

while True:
    interface  = input("1. Load, 2. Dump, 3. Add, 4. Del, 5. Exit")
    if interface == "5":
        break
    elif interface == "1":
        with open(path, "r") as max:
            list_var = json.load(max)
        print(list_var)
    elif interface == "2":
        with open(path, "w") as oleg:
            json.dump([int(i) for i in input("Enter your number").split()], oleg) # dump- для серіалізації даних
    elif interface == "3":
        with open(path, "r") as oleg:
            list_var = json.load(oleg)
        list_var = list_var + [int(i) for i in input("Enter your number").split()]
        with open(path, "w") as max:
            json.dump(list_var,max)
    elif interface == "4":
        with open(path, "r") as oleg:
            list_var = json.load(oleg)
        del_number = [int(i) for i in input("Enter your number").split()]
        for element in del_number:
            list_var.remove(element)
        with open(path, "w") as max:
            json.dump(list_var,max)


# task 4

# path = os.path.join("data_base", "test.json")

# a = input("Add new pass:\n")
# with open(path, "r") as rd:
#     pass_let = json.load(rd)
# pass_let.append(a)

# with open(path, "w") as num:
#     json.dump(pass_let, num)

# task 5

# path = os.path.join("data_base", "test.json")
#
# a = input("Your pass:\n")
# with open(path, "r") as rd:
#     pass_let = json.load(rd)
# if a in pass_let:
#     print("Yes")
# else:
#     print("No")













