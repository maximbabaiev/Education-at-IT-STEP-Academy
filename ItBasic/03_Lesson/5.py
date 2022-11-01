number = 5
count = 0

while count < 5:
    number += 1
    if (number % 2) == 1:
        continue
    print(number)
    count += 1