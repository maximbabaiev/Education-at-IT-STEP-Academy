file1 = open("file1.txt", 'r')  # открыли первый файл для считывания
file2 = open("file2.txt", 'r')  # открыли второй файл для считывания

file1_lines = file1.readlines()  # считываем файлы построчно
file2_lines = file2.readlines()

for i in range(len(file1_lines)):   # пошли цыклом по длинне первого файла
    if file1_lines[i] != file2_lines[i]:    # если файлы не равны
        print("Line " + str(i+1) + " doesn't match.")   # номер строки по счету в которой найдены разные строки
        print("------------------------")
        print("File1: " + file1_lines[i])   # выводим разницу в первом файле
        print("File2: " + file2_lines[i])   # и во втором

file1.close()   # закрываем файлы
file2.close()