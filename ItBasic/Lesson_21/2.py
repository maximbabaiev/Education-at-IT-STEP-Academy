import os.path

quantity = int(input("How much numbers do you want to save?"))

while quantity > 0:
    name = input("Please, input name:\n")
    number = input("Please, input phone number:\n")

    path1 = os.path.join("data_base", "test2.txt")

    fileObj = open(path1, 'a')
    fileObj.write(name + " " + number + "\n")

    quantity = quantity - 1

    fileObj.close()
