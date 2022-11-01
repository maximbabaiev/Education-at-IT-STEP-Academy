import os.path


class Money:
    def __init__(self, name, money, penni, valuta):
        self.name = name
        self.money = money
        self.penni = penni
        self.valuta = valuta
        self.curs = {'UAH': {'UAH': 1, 'USD': 42, 'EUR': 41}, 'USD': {'UAH': 0.025, 'USD': 1, 'EUR': 0.025},
                     'EUR': {'UAH': 0.024, 'USD': 0.98, 'EUR': 1}}
        self.path = os.path.join("data_file", "discount.txt")
        file = open(self.path, "r")
        dara_read = file.readlines()
        for line in dara_read:
            if name in line:
                self.discount = float(line.split()[1])
                break
            else:
                self.discount = 0
        file.close()

    def __repr__(self):
        return f' {self.money}.{self.penni} {self.valuta}'

    def sell(self, product):

        if 0 <= self.discount < 500:
            product_money = product.money * self.curs.get(self.valuta).get(product.valuta)
            product_penni = product.penni * self.curs.get(self.valuta).get(product.valuta)
            if product_penni > 100:
                product_money = product_money + product_penni // 100
                product_penni = product_penni % 100
            if self.money > product_money:
                self.penni = self.penni - product_penni
                self.money -= product_money
                self.discount += product_money + product_penni / 100
            else:
                return f'You don t have money'

        if 500 < self.discount < 1000:
            product_money = product.money * self.curs.get(self.valuta).get(
                product.valuta) - product.money * self.curs.get(self.valuta).get(product.valuta) * 0.05
            product_penni = product.penni * self.curs.get(self.valuta).get(
                product.valuta) - product.penni * self.curs.get(self.valuta).get(product.valuta) * 0.05
            if product_penni > 100:
                product_money = product_money + product_penni // 100
                product_penni = product_penni % 100
            if self.money > product_money:
                self.penni = self.penni - product_penni
                self.money -= product_money

                self.discount += product_money + product_penni / 100

            else:
                return f'You don t have money'

        if self.discount > 1000:
            product_money = product.money * self.curs.get(self.valuta).get(
                product.valuta) - product.money * self.curs.get(self.valuta).get(product.valuta) * 0.1
            product_penni = product.penni * self.curs.get(self.valuta).get(
                product.valuta) - product.penni * self.curs.get(self.valuta).get(product.valuta) * 0.1
            if product_penni > 100:
                product_money = product_money + product_penni // 100
                product_penni = product_penni % 100
            if self.money > product_money:
                self.penni = self.penni - product_penni
                self.money -= product_money
                self.discount += product_money + product_penni / 100
            else:
                return f'You don t have money'
        file = open(self.path, "r")
        data_read = [line for line in file if not self.name in line]
        data_read.append(f"{self.name} {self.discount}")
        file.close()
        file = open(self.path, "w")
        file.write("\n".join(data_read))
        file.close()
        return f'{product} {int(self.money)} {int(self.penni)} {self.valuta} '


class Product(Money):
    def __init__(self, money, penni, valuta, name):
        super().__init__(name, money, penni, valuta)

    def __repr__(self):
        return f'{self.money} {self.penni} {self.valuta}'


def shop():
    path = os.path.join('data_file', 'file.txt')
    file = open(path, 'r')
    file1 = file.read().split("\n")
    file.close()
    return '\n'.join(file1)


def add(product):
    path = os.path.join('data_file', 'file.txt')
    file = open(path, 'a')
    file.write(f'\n{product.name} {product.money} {product.penni} {product.valuta}')
    file.close()
    return "Okay"
