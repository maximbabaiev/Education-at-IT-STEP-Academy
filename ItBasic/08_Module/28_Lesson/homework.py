def firstNum(max):
    number = 2
    divider = 2

    while number <= max:
        if number == divider:
            yield number
            divider = 2
            number += 1
        if number % divider != 0:
            divider += 1
            if number == divider:
                yield number
                divider = 2
                number += 1
        else:
            divider = 2
            number += 1


f = firstNum(30)

for el in range(1, 9):
    print(next(f))
