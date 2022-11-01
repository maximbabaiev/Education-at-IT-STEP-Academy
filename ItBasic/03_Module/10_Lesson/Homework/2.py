from itertools import chain

tuple1 = (10, 2, 3, 5, 6, 7, 8, 78, 98, 56, 67)
tuple2 = (11, 2, 3, 5, 6, 7, 8, 45, 34, 56, 67)
tuple3 = (2, 3, 5, 6, 7, 8, 56, 67)


def unique():
    lst = [list(tuple1), list(tuple2), list(tuple3)]
    uni = list(chain.from_iterable(lst))
    return [i for i in set(uni) if uni.count(i) == 1]


print(unique())
