class Devise:
    def __init__(self, name, color):
        self.color = color
        self.name = name

    def __repr__(self):
        return f"{self.name}, {self.color}"


class CoffeeMachine(Devise):
    def __init__(self, name, color, id_cod):
        Devise.__init__(self, name, color)
        self.id_cod = id_cod

    def __repr__(self):
        return f"{self.id_cod}, {self.name}, {self.color}"


class Blender(Devise):
    def __init__(self, name, color, wight):
        Devise.__init__(self, name, color)
        self.wight = wight

    def __repr__(self):
        return f"{self.name}, {self.color}, {self.wight}"


class MeatGrinder(Devise):
    def __init__(self, name, color, prise):
        Devise.__init__(self, name, color)
        self.prise = prise

    def __repr__(self):
        return f"{self.name}, {self.color}, {self.prise}"

coffe = CoffeeMachine("1", "red", "11111")
print(coffe)
blender = Blender("1", "2", "60")
print(blender)
meat = MeatGrinder("1", "2", "34$")
print(meat)


