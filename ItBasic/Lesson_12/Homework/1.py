tuple1 = (10, 2, 3, 5, 6, 7, 8, 78, 98, 56, 67)
tuple2 = (11, 2, 3, 5, 6, 7, 8, 45, 34, 56, 67)
tuple3 = (2, 3, 5, 6, 7, 8, 56, 67)

res = tuple(set(tuple1) and set(tuple2) and set(tuple3))

print(res)












