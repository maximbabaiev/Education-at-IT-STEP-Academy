import json
import os.path
from easygui import *

path = os.path.join("data_base", "capitals_list.json")

while True:
    interface = buttonbox("Choise action: ", "List of state capitals", ["ADD", "DEL", "SEARCH", "Edit", "EXIT"])
    if interface == "ADD":
        data = multenterbox("Enter your data: ", "List of state capitals", ["Country", "Capital"])
        with open(path, "r") as file:
            old_data = json.load(file)
        old_data[data[0]] = data[1]
        with open(path, "w") as file:
            json.dump(old_data, file)
            msgbox('\n'.join([f'Login: {element}, password: {old_data.get(element)}' for element in old_data]))

    elif interface == "DEL":
        del_data = enterbox("Country: ")
        with open(path, "r") as file:
            old_data = json.load(file)
        old_data.pop(del_data)
        with open(path, "w") as file:
            json.dump(old_data, file)

    elif interface == "SEARCH":
        with open(path, "r") as file:
            old_data = json.load(file)
        data = multenterbox("Enter your Country: ", "List of state capitals", ["Country"])



    else:
        break