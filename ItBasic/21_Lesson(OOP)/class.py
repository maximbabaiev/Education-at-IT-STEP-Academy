

class Person:
    def __init__(self, name_par, data_par, tel_par, citi_par, country_par):
        self.name = name_par
        self.data = data_par
        self.tel = tel_par
        self.citi = citi_par
        self.country = country_par
    # def hello(self):
    #     return "Hello, my name is"
    # def __str__(self):
    #     return f"{self.name}, {self.age}, {self.work}"
    # def birthday(self):
    #     self.age = str(int(self.age) + 1)
    #     return "Happy birthday"
    def change_name(self, new_name):
        self.name = new_name
        return "Saved"
    def __str__(self):
        return f"{self.name}, {self.data}, {self.tel}, {self.citi}, {self.country}"

saha = Person(name_par="Saha", data_par="10-10-10", tel_par="0997755443", citi_par="Kharkiv",country_par="Ukraine" )
print(saha)
print(saha.change_name("Max"))
print(saha)





