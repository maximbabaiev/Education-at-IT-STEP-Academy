# class Car:
#     def run(self):
#         return "rrrrrr"
#
#
# class LitleCar(Car):
#     def run(self):
#         return "rrrrrrrrrrrrr"
#
#     def speed(self):
#         return "i have 240km"
#
#
#
#
#
# car1 = LitleCar()
# print(car1.run())
# print(car1.speed())


# class Bird:
#     def fly(self):
#         return "I can FLY"
#
#
# class Horse:
#     def run(self):
#         return "I can run"
#
#
# class Pegas(Bird, Horse):
#     pass
#
#
# bob = Pegas()
#
# print(bob.fly() + " " + bob.run())


# class Human:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def sum(self, a, b):
#         return a + b
#
#     def __repr__(self):
#         return f"{self.name}, {self.age}"
#
#
# class Builder(Human):
#     def per(self, side1, side2):
#         per = side1 * 2 + side2 * 2
#         return per
#
# side1 = input()
# side2 = input()
# rob = Builder(name="rob", age="25")
# rob.per()
#
#
# bob = Builder(age=14, name="Sasha", width=14, height=15)
# print(bob)
#
#
# class Sailor(Human):
#     pass
#
#
# class Pilot(Human):
#     pass


# class Passport:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"{self.age}, {self.name}"
#
#
# class ForeignPassport(Passport):
#     def __init__(self, age, name, country):
#         super().__init__(age, name)
#         self.anoser = country
#
#     def __repr__(self):
#         return f"{self.age}, {self.name}, {self.anoser}"
#
#
# bob = ForeignPassport(age="24", name="bob", country="UA")
#
# print(bob)

class Tvaruna:
    def __init__(self, name, vid):
        self.name = name
        self.vid = vid

    def __repr__(self):
        return f"{self.name}, {self.vid}"


class Tigr(Tvaruna):
    pass


class Krokodil(Tvaruna):
    pass


class Kenguru(Tvaruna):
    def __init__(self, name, vid, kol_lap):
        super().__init__(name, vid)
        self.kol_lap = kol_lap

    def __repr__(self):
        return f"{self.name}, {self.vid}, {self.kol_lap}"


kenguru = Kenguru("name", "vid", "4")

print(kenguru)
