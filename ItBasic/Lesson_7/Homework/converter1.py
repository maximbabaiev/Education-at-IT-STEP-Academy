dlina = int(input("1. Метры в мили\n 2. Метры в дюймы\n 3. Метры в ярды\n"))
if dlina == 1:
    value_dlina = float(input("Сколько метров? : \n"))
    print(value_dlina, "Метров =", round(value_dlina * 0.00062), "миль")
elif dlina == 2:
    value_dlina = float(input("Сколько метров? : \n"))
    print(value_dlina, "Метров =", round(value_dlina * 39.37), "дюймов")
elif dlina == 3:
    value_dlina = float(input("Сколько метров? : \n"))
    print(value_dlina, "Метров =", round(value_dlina * 1.09), "ярдов")



