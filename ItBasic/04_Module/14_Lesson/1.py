def meanF(*args):
    s = 0
    k = 0
    for i in args:
        s += i
        k += 1
    return s / k


print("(1+2+3)/3=", meanF(1, 2, 3))
