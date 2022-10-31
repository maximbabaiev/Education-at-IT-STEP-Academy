a = str(input("Введите ваше имя: "))
b = str(input("Введите ваш пол: "))
c = int(input("Введите ваш вес: "))
d = int(input("Введите ваш рост: "))
if b == "Man":
    r = int(d - 100) * 1.15
elif b == "Woman":
    r = int(d - 110) * 1.15
print(a, "Ваш идеальный вес", r, "kg")
