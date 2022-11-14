import json
import os.path
from easygui import *

# Task 1

# path = os.path.join("data_base2", "worker_list.json") #
# while True:
#     interface = buttonbox("Choise action: ", "Dictionary", ["ADD", "DEL", "SEARCH", "ALL", "EXIT"])
#     if interface == "ADD":
#         data = multenterbox("Enter your data: ", "Employees", ["Name","Age","Work"]) # ["Oleg", "25", "teacher"]
#         with open(path, "r") as file:
#             old_data = json.load(file)
#         old_data[data[0]] = {"Age": data[1], "Work": data[2]}
#         with open(path, "w") as file:
#             json.dump(old_data,file)
#     elif interface == "DEL":
#         del_data = enterbox("Name: ")
#         with open(path, "r") as file:
#             old_data = json.load(file)
#         old_data.pop(del_data)
#         with open(path, "w") as file:
#             json.dump(old_data, file)
#     elif interface == "SEARCH":
#         with open(path, "r") as file:
#             old_data = json.load(file)
#         data = multenterbox("Enter your data: ", "Employees", ["Name par", "Param"])
#         msg_box = ""
#         for element in old_data:
#             if data[1] == old_data.get(element).get(data[0]):
#                 msg_box = msg_box + f'Name: {element}, Age: {old_data.get(element).get("Age")}, Work: {old_data.get(element).get("Work")}\n'
#         # msgbox(msg_box)
#         # msgbox("\n".join([f'Name: {element}, Age: {old_data.get(element).get("Age")}, Work: {old_data.get(element).get("Work")}' for element in old_data if data[1] == old_data.get(element).get(data[0])]))
#     elif interface == "ALL":
#         with open(path, "r") as file:
#             old_data = json.load(file)
#         msgbox("\n".join([f'Name: {element}, Age: {old_data.get(element).get("Age")}, Work: {old_data.get(element).get("Work")}' for element in old_data]))
#     else:
#         break

# Task 2

# path = os.path.join("data_base2", "pass_list.json")
#
# while True:
#     interface = buttonbox("Choise action: ", "Dictionary", ["ADD", "DEL", "SEARCH", "Edit", "EXIT"])
#     if interface == "ADD":
#         data = multenterbox("Enter your data: ", "Employees", ["Login", "Pass"])
#         with open(path, "r") as file:
#             old_data = json.load(file)
#         old_data[data[0]] = data[1]
#         with open(path, "w") as file:
#             json.dump(old_data, file)
#             # msgbox('\n'.join([f'Login: {element}, password: {list1.get(element)}' for element in list1]))
# #
# #
#     else:
#         break





