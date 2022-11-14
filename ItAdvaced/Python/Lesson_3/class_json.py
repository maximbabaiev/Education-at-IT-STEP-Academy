import os.path
import json
from easygui import *




# "BMW 920", "2020", "Germany", "5.5", "red", "50000"
class Cars:
    def __init__(self, model_par, age_par, producer_par, capacity_par, color_par, price_par, win_code_par):
        # self.model[model_par] = model_par
        self.model = model_par
        self.age = age_par
        self.producer = producer_par
        self.capacity = capacity_par
        self.color = color_par
        self.price = price_par
        # self.win_cod[win_cod_par] = {self.model, self.age, self.producer, self.capacity, self.color, self.price}
        self.win_code = win_code_par

    def __repr__(self):
        return f'{self.model}, {self.age}, {self.producer}, {self.capacity}, {self.color}, {self.price}, {self.win_code}'

    def change_model(self, new_model):
        self.model = new_model
        return "Saved"

    def change_age(self, new_age):
        self.age = new_age
        return "Saved"

    def change_producer(self, new_producer):
        self.producer = new_producer
        return "Saved"

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity
        return "Saved"

    def change_color(self, new_color):
        self.color = new_color
        return "Saved"

    def change_price(self, new_price):
        self.price = new_price
        return "Saved"


class Car_showroom:

    def __init__(self, file_name):
        self.file_name = file_name + ".json"
        self.path = os.path.join("", self.file_name)

    def add_car(self, new_car):
        with open(self.path, "r") as file1:
            a_car = json.load(file1)
        a_car[new_car.win_code] = {"model": new_car.model, "age": new_car.age, "producer": new_car.producer,
                                   "capacity": new_car.capacity, "color": new_car.color, "price": new_car.price}
        with open(self.path, "w") as file1:
            json.dump(a_car, file1, indent=4)
        return f'Tour {new_car} successfully added'

    def oll_car(self):
        with open(self.path, "r") as file1:
            file = json.load(file1)
        return " ".join([f"{item}, {file.get(item).get('model')}, {file.get(item).get('age')}, {file.get(item).get('producer')}, "
                         f"{file.get(item).get('capacity')},  {file.get(item).get('color')}, "
                         f"{file.get(item).get('price')}" for item in file])

    def __repr__(self):
        return self.file_name

    def rem_car(self, remove_car):
        with open(self.path, "r") as file1:
            file = json.load(file1)
        file.pop(remove_car.win_code)
        with open(self.path, "w") as file1:
            json.dump(file, file1)
        return f'Your {remove_car.model} sold'

    def update_car(self, update_car):
        with open(self.path, "r") as file1:
            file = json.load(file1)
        file[update_car.win_code] = {"model": update_car.model, "age": update_car.age, "producer": update_car.producer,
                                   "capacity": update_car.capacity, "color": update_car.color, "price": update_car.price}
        with open(self.path, "w") as file1:
            json.dump(file, file1)
        return f'Your {update_car} update'

    def unicAuto(self, unic_1, unic_2):
        with open(self.path, "r") as file1:
            file = json.load(file1)
        dict_war1 = file.get(unic_1.win_code)
        dict_war2 = file.get(unic_2.win_code)
        for key in dict_war1:
            print(dict_war1.get(key), dict_war2.get(key))


BMW920 = Cars("BMW 920", "2020", "Germany", "5.5", "red", "50000", "05561")
Reno20 = Cars("Reno 20", "2018", "France", "5.0", "black", "45000", "156565")

avtosalon = Car_showroom("avtosalon")
print(avtosalon.add_car(BMW920))
# print(avtosalon.add_car(Reno20))
avtosalon.unicAuto(BMW920, Reno20)
# print(BMW920.change_color("Green"))
# print(avtosalon.update_car(BMW920))
# print(avtosalon.oll_car())
# avtosalon.rem_car(Reno20)