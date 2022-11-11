# получение итератора итерабельного объекта

iterable = range(10)

iter_obj = iter(iterable)

# безсконечный цикл
while True:
    try:
        # получение следующего елемента
        element = next(iter_obj)
        print(element)
        # какие-то операции над элементом
    except StopIteration:
        # Если получили StopIteration, выходим из цикла
        print('stop')
        break
