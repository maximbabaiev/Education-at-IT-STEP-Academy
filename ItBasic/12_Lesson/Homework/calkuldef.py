def wh(first):
    print(first + first ** 2 + first ** 3)


wh(10)


def let(first, second):
    for i in range(first, second + 1):
        if i % 2 == 0:
            print(i)


let(11, 15)
