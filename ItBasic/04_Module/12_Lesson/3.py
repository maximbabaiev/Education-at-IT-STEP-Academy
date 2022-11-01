
x = float(input("x"))

y = float(input("y"))

def calcul(a, b):

    return a + b


if calcul(x, y) <= 0:

    y = 5 * x + 2 * y

else:
    y = 10 * x - 3 * y

print("y = ", y)