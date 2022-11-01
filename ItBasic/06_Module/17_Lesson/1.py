
def sum(x, y):
    if x == y:
        return x
    else:
        return y + sum(x, y - 1)

print(sum(2, 5))
