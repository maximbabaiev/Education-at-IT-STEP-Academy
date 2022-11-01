import os.path


path = os.path.join("data_base", "test3.txt")
math = os.path.join('data_base', 'test2.txt')
file1 = open(path, 'r')
file2 = open(math, 'w')

file_read = file1.read()
new_file = ""

