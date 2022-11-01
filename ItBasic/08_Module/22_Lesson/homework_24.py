class Nikola:
    def __init__(self, name):
        if name == "Nikola":
            self.name = name
        else:
            self.name = f"Я не {name} а Nikola"

    def __repr__(self):
        return f"{self.name}"


nikola = Nikola(name="Nikola")
print(nikola)

# class Soda:
#     def __init__(self, lemon):
#         self.lemon = lemon
#
#     def __repr__(self):
#         return f"{self.lemon}"
#
#     def show_my_drink(self):
#         if self.lemon == "":
#             return f"Вода газированная"
#         else:
#             return f"Вода газированная с добавкой {self.lemon}"
#
#
# soda = Soda(lemon="lemon")
#
# print(soda.show_my_drink())
