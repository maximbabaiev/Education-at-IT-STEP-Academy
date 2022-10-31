my_list = [45, 43, 56, 78, 89, 23]


def countPrimeNumbers(numbers):
    count_prime = 0
    for num in numbers:
        if num < 2:
            continue
        else:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                count_prime += 1
    return count_prime


print(countPrimeNumbers(my_list))
