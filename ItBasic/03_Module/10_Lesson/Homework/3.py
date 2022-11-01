tuple1 = (10, 2, 3, 9)
tuple2 = (10, 2, 3, 8)
tuple3 = (10, 2, 3, 5)

tuple4 = tuple1 + tuple2 + tuple3

resul = tuple(i for i, j in enumerate(tuple4) if tuple4.count(j) > 1)

print(tuple4)
print(resul)
