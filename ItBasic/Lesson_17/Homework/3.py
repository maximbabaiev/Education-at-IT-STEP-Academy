list1 = [12, 34, 56, 67, 45, -11, -14]




def fun(*args):
    twin_numbers = []
    [twin_numbers.append(e) for e in args if e % 2 == 0]
    not_paired = []
    [not_paired.append(e) for e in args if e % 2 != 0]
    positive = []
    [positive.append(e) for e in args if e > 0]
    negative = []
    [negative.append(e) for e in args if e < 0]
    return print(len(twin_numbers)), len(not_paired), len(positive), len(negative)


print(fun(*list1))

