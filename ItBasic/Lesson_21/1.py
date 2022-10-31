import os.path


path = os.path.join("data_base", "test3.txt")
file1 = open(path, 'w')
user_name = input("введите ваше имя")

file1.write(user_name)
file1.close()