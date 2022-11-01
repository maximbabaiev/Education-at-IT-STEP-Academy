import os.path
#
# path1 = os.path.join("", "text1.txt")
# path2 = os.path.join("", "text2.txt")
#
# file1 = open(path1, "r")
# file2 = open(path2, "w")
#
# file_read1 = file1.read()
# mylist = list(file_read1.split(" "))
# for element in mylist:
#     if not element.startswith("Assyr"):
#         file2.write(element + " ")
#
# file1.close()
# file2.close()


path1 = os.path.join("data_base", "Txt1.txt")
path2 = os.path.join("data_base", "Txt2.txt")
file1 = open(path1, "r")
file_1 = file1.read().replace(",", "").replace(".", "").split()
file2 = open(path2, "r")
file_2 = file2.read().split()
new_line = [elem for elem in file_1 if elem not in file_2]
file1.close()
file2.close()
path1 = os.path.join("data_base", "Txt1.txt")
file1 = open(path1, "w")
[file1.write(elem + " ") for elem in new_line]
file1.close()

