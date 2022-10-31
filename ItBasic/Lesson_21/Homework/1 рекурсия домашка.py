def exp(x, y):  #создали функцию
    if y == 0:  # любое число, кроме нуля, возведенное в нулевую степень, будет равно единице:
        return 1
    else:
        return x * exp(x, y - 1)


n = int(input("Enter the first number:"))
m = int(input("Enter the second number:"))
print("Result=", exp(n, m))

