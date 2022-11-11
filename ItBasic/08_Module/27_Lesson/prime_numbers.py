class Prime:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        x = self.current
        self.current += 1
        for num in range(self.current, self.n):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    return num


p = Prime(n=10)

c = iter(p)

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))