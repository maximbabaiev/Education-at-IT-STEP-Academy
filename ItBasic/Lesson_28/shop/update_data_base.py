from easygui import *
from func import *

add_data = multenterbox("Enter data", "Shop", ["Name:", "Money:", "Penni:", "Valuta:"])
product = Product(name=add_data[0], money=int(add_data[1]), penni=int(add_data[2]), valuta=add_data[3])
print(add(product))