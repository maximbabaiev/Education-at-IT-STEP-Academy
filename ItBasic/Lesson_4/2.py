price1 = int(input())
price2 = int(input())
price3 = int(input())
discount = int(input())
ad = price1 + price2 + price3
m1 = ad * discount / 100
m2 = ad - m1
print("АТБ Маркет")
print("Касир : Иван Иванов")
print("Тов 1", price1)
print("Тов 2", price2)
print("Тов 3", price3)
print("Скидка : ", discount, "%", sep="")
print("Всего без скидки : ", ad)
print("Всего к оплате: ", m2)
print("02.08.2022")

