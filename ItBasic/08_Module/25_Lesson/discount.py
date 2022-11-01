import os.path


class Money:
    def __init__(self, cili, cop, valuta):
        self.cili = cili
        self.cop = cop
        self.valuta = valuta
        self.exchange = {
            "UAH": {
                "UAH": 1,
                "USD": 42,
                "EUR": 41
            },
            "USD": {
                "UAH": 0.025,
                "USD": 1,
                "EUR": 0.025
            },
            "EUR": {
                "UAH": 0.24,
                "USD": 0.98,
                "EUR": 1
            }

        }
        self.discount = 0

    def __repr__(self):
        return f"{self.cili}.{self.cop} {self.valuta}, {self.discount}"

    def sellDiscount(self, product):
        money_sum = self.cili * 100 + self.cop
        product_sum = (product.cili * self.exchange.get(self.valuta).get(product.valuta) * 100 + (
                    product.cop + self.exchange.get(self.valuta).get(product.valuta)))
        if money_sum > product_sum:
            money_sum = money_sum - (product_sum - product_sum * self.discount)
            if self.discount < 0.1:
                self.discount += 0.005
            else:
                self.discount = 0.1
            self.cili = int(money_sum/100)
            self.cop = int(str(int(money_sum)))[-2::]
            viz_cop = str(int(money_sum))[-2::]
        else:
            return "You don't have enough money to make exchange"
        return f"С вас списано: {product}\n Остаток: {self.cili}.{viz_cop} {self.valuta} Discount: {self.discount}"






class Product(Money):
    pass
#     def __init__(self, cili, cop, valuta, name):
#         super(Product, self).__init__(cili, cop, valuta)
#         self.name = name
#         self.path = os.path.join("data", "file_for_money.txt")
#         file = open(self.path, "a", encoding="utf-8")
#         file.write(f"Назавние продукта :{self.name}, {self.cili}, {self.cop}, {self.valuta} \n")
#         file.close()
#
#     def __repr__(self):
#         return f"{self.name}, {self.cili}, {self.cop}, {self.valuta}"
#
#     def allTovar(self):
#         file = open(self.path, "r", encoding="utf-8")
#         file1 = file.readlines()
#         file.close()
#         return "".join(file1)


money = Money(cili=5000, cop=75, valuta="USD")
coffe = Product(42, 00, "UAH")
print(money.sell(coffe))




