import os.path

path1 = os.path.join("", "test2.txt")


option = input("If you want to read contact push 1: \n"
               "If you want to add contact push 2 \n")


if option == "1":
    fileObj = open(path1, 'r')
    name = input("Please, input your contact's name: ")
    for element in fileObj:
        if element.startswith(name):
            print(element)
    fileObj.close()

elif option == "2":
    fileObj = open(path1, 'a')
    new_name = input("Please, input name: ")
    new_number = input("Please, input number: ")
    fileObj.write(new_name + " " + new_number + "\n")
    fileObj.close()

else:
    print("Looks like you're wrong. THINK, than try again.")