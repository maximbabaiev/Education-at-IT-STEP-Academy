class Car:
    def __init__(self, name_model_par, release_year_par, manufacturer_par, engine_volume_par, color_par, prise_par):
        self.name = name_model_par
        self.release = release_year_par
        self.manufac = manufacturer_par
        self.volume = engine_volume_par
        self.color = color_par
        self.prise = prise_par

    def __str__(self):
        return f"{self.name}, {self.release}, {self.manufac}, {self.volume}, {self.color}, {self.prise}"

    def nameModel(self):
        return f"{self.name}"

    def releaseYear(self):
        return f"{self.release}"

    def manuFacturer(self):
        return f"{self.manufac}"

    def engineVolume(self):
        return f"{self.volume}"

    def colorCar(self):
        return f"{self.color}"

    def priseCar(self):
        return f"{self.prise}"

    def changeModel(self, new_model):
        self.name = new_model
        return "Done"


toyota = Car(name_model_par="Toyota", release_year_par="2022", manufacturer_par="Toyota Motor Corporation", engine_volume_par="2.5", color_par="Black", prise_par="50000$")
print(toyota)
print(toyota.changeModel("Mazda"))
print(toyota)


