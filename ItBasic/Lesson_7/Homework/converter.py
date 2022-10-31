dlina = int(input(' 1. Мили -> километры\n 2. Ярды -> метры\n 3. Футы -> метры\n 4. Дюймы -> сантиметры\n'))
if dlina == 1:
    value_dlina = float(input('Сколько миль? :\n'))
    print(value_dlina, 'миль =', round((value_dlina / 0.621371), 2), 'километров')
elif dlina == 2:
    value_dlina = float(input('Сколько ярдов? :\n'))
    print(value_dlina, 'ярдов =', round((value_dlina / 0.9144), 2), 'метров')
elif dlina == 3:
    value_dlina = float(input('Сколько футов? :\n'))
    print(value_dlina, 'футов =', round((value_dlina / 3.28084), 2), 'метров')
elif dlina == 4:
    value_dlina = float(input('Сколько дюймов? :\n'))
    print(value_dlina, 'дюймов =', round((value_dlina / 0.393701), 2), 'сантиметров')
