

def para(a, b):
    if a > b:
        return
    print(a, end=' ')
    return para(a + 2, b)


print(para(10, 19))