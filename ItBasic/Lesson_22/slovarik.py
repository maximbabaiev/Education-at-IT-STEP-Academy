import os.path
from easygui import *

path1 = os.path.join("data_base", "slovnik.txt")

while True:
    interface = buttonbox("Виберіть дію: ", "Словник", ["Додати", "Видалити", "Екзамен", "Пошук", "Вихід"])
    if interface == "Додати":
        words = multenterbox("Enter your world: ", "Словник", ["Англійська", "Українська"])
        file = open(path1, 'a')
        # file.write(f'{words[0]} {words[1]}\n')
        file.write(" ".join(words) + "\n")
        # всі елементи які будуть в world будуть додані в файл і записані в один рядок через пробіль
        file.close()
    elif interface == "Пошук":
        word = enterbox("Напишіть своє слово")
        file = open(path1, 'r')
        for line in file:
            if line.startswith(word + " ") or line.endswith(word + "\n"):  # якщо інгліш слово ми ввели
                msgbox(line.replace(word, ""))  # ми заміняємо інгліш слово на пустоту у файлі і виводиться тільки укр
        file.close()
    elif interface == "Видалити":
        word = enterbox("Напишіть своє слово")
        file = open(path1, 'r')
        list_lines = []
        # створили ящик в який кидаємо файли, які не починаються і не закінчуються на наше слово
        for line in file:
            if not line.startswith(word + " ") and not line.endswith(word + "\n"):
                list_lines.append(line)
        # list_lines = [line for line in file if not line.startswith(word+ " ") and not line.endswith(word + "\n")]
        file.close()
        file = open(path1, 'w')
        # метод оупена W - відкриває пустий файл і приймає що ми туда хочемо писати.
        file.write("".join(list_lines))
        # показуємо перезаписаний файл де вже є тільки створений наш ящик і тим самим видаляємо вказане слово
        file.close()
    elif interface == "Екзамен":
        file = open(path1, 'r')
        rate = 0
        readFile = file.readlines()
        mode = buttonbox("Оберіть мову для екзаменого перекладу", "Екзамен", ["En", "Ua"])
        if mode == "En":
            for line in readFile:
                words = line.split()
                pitania = enterbox(f"Скажіть переклад слова - {words[1]}")
                pitania = pitania.lower()
                if pitania == words[0]:
                    rate += 1
        else:
            for line in readFile:
                words = line.split()
                pitania = enterbox(f"Скажіть переклад слова - {words[0]}")
                pitania = pitania.lower() #перетворюємо усі слова, які ввелись нижче - у малий реєстр, за допомогою метода
                if pitania == words[1]:
                    rate += 1
        msgbox(f"Ви вгадали: {rate} слова з {len(readFile)}!")
    else:
        break