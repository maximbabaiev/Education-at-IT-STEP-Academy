import os.path
from easygui import *

path = os.path.join("data_base", "en-ua.txt")

while True:
    interface = buttonbox("Choise action: ", "Dictionary", ["ADD", "DEL", "EXAM", "SEARCH", "EXIT"])
    if interface == "EXIT":
        break
    elif interface == "ADD":
        words = multenterbox("Enter your words: ", "Dictionary", ["En", "Ua"])
        file = open(path, "a", encoding="utf-8")
        # file.write(f'{words[0]} {words[1]}\n')
        file.write(" ".join(words) + "\n")
        file.close()
    elif interface == "SEARCH":
        word = enterbox("Enter your word")
        file1 = open(path, 'r')
        for i in file1:
            print(word)
    elif interface == "EXAM":
        file = open(path, "r")
        rate = 0
        read_file = file.readlines()
        for line in read_file:
            words = line.split()
            question = enterbox(f'Enter translate word - {words[0]}')
            if question == words[1]:
                rate += 1
        msgbox(f"you guessed  {rate} words out of {len(read_file)}")
