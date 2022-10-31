list1 = [12, 34, 56, 67, 45]


def sumElement(list_sum):  # создаем функцию
    total = 0              # создаем переменную кторая будет выводить суму чисел в списке
    i = 0
    while i < len(list_sum):    # пошли цыклом
        total = total + list_sum[i]     # плюсуем все числа в списке
        i = i + 1                       # цыкл остановится когда i == длине списка
    return total                        # возвращаем суму чисел


print(sumElement(list1))
