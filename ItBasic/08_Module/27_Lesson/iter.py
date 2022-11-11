# class Range:
#
#     def __init__(self, max):
#         self.max = max
#
#     def __iter__(self):
#         self.count = 0
#         self.last_numbers = 0
#         return self
#
#     def __next__(self):
#         self.last_numbers += 1
#         self.count += 1
#         if self.count > self.max:
#             raise StopIteration
#         return self.last_numbers
#
#
# a = Range(10)
# for number in a:
#     print(number)


# class Factorial:
#     def __init__(self, max):
#         self.max = max
#
#     def __iter__(self):
#         self.last_numbers = 0
#         self.count = self.last_numbers + 1
#         return self
#
#     def __next__(self):
#         self.last_numbers = self.count * self.last_numbers
#
#


# class PrimeNumbers:
#     def __init__(self, n):
#         self.prime_numbers = []
#         self.n = n
#         self.i = 0
#
#     def __iter__(self):
#         self.i = 1
#         return self
#
#     def get_prime(self):
#         self.i += 1
#         for prime in self.prime_numbers:
#             if self.i % prime == 0:
#                 return False
#         return True
#
#     def __next__(self):
#         while self.i < self.n:
#             if self.get_prime():
#                 self.prime_numbers.append(self.i)
#                 return self.i
#         else:
#             raise StopIteration()
#
#
# prime_number_iterator = PrimeNumbers(n=5)
# for number in prime_number_iterator:
#     print(number)


class PrimeNumbers:
    def __init__(self, chislo):
        self.chislo = chislo

    def __iter__(self):
        self.i = 2
        self.prime_numbers = []
        return self

    def __next__(self):
        while self.i <= self.chislo:
            for prime in self.prime_numbers:
                if self.i % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.i)
                return self.i
            self.i += 1
        else:
            raise StopIteration()


prime_number = PrimeNumbers(chislo=5)
for number in prime_number:
    print(number)
