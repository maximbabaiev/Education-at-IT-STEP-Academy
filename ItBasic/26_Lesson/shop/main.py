from easygui import *
from func import *


money = Money(name="Max", money=20000, penni=75, valuta='UAH')


shop_cart = buttonbox(f"{shop()}", "Shop cart", [name.split()[0] for name in shop().split("\n")])

product = shop().split('\n')
for i in product:
    if shop_cart in i:
        list_data = i.split()
        product = Product(name=list_data[0], money=int(list_data[1]), penni=int(list_data[2]), valuta=list_data[3])

print(money.sell(product))
# coffe = Product(name='coffe',money=20, penni=25, valuta='UAH')
# latte = Product(name='latte',money=2, penni=1, valuta='EUR')
# a = Product(name='a', money=100, penni=25, valuta='UAH')
# b = Product(name='b', money=50, penni=25, valuta='EUR')

# print(money)
# print(money.sell(coffe))
# print(money)
# print(coffe.shop())
# print(money.sell(b))
# print(money.sell(a))


