from random import randint

list1 = [randint(1, 100) for i in range(randint(6, 15))]  # рандомное заполнение списка числами от 1 до 100
print(list)

list1[0], list1[-1] = list1[-1], list1[0]  # смена местами последнего и первого элемента
print(list1)
