class Money:
    def __init__(self, cili, cop, valuta):
        self.cili = cili
        self.cop = cop
        self.valuta = valuta

    def __repr__(self):
        return f"{self.cili}.{self.cop} {self.valuta}"

    def sell(self, product):
        if self.valuta == product.valuta:
            if self.cili > product.cili:
                if self.cop < product.cop:
                    self.cili -= 1
                    self.cop += 100
                self.cop = self.cop - product.cop
                self.cili -= product.cili
                return "Смачного!"
            else:
                return "Вам не вистачить грошей"


class Product(Money):
    pass


money = Money(cili=50, cop=75, valuta="UAH")
coffe = Product(cili=25, cop=25, valuta="UAH")
print(money)
print(money.sell(coffe))
print(money)


