import os.path


path = os.path.join("../19_Lesson/data_base", "test3.txt")
math = os.path.join('../19_Lesson/data_base', 'test2.txt')
file1 = open(path, 'r')
file2 = open(math, 'w')
split_var = file1.read().split()
print(split_var)
for i in split_var:
    if len(i) >= 7:
        file2.write(i + ' ')

file1.close()
file2.close()
