#
# print(-1.1)
# print(+2)
# print(2 % 6 % 9)
# print(2 ** 2 ** 3)
# print(2 * 3 % 5)
# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# a = 3.0
# b = 4.0
# c = (a ** 2 + b ** 2) ** 0.5
# print("c =", c)
# var /= 5 * 2
# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# year = 2000
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#  print("Year", year, "is leap")
# car_speed = 130
# car_speed += 40
# print(car_speed)
# amount = int(input("Enter the amount of received items: "))
# items_type = input("Specify the type of received items: ")
# line = input("Enter some string: ")
# for c in line[0 : 10 : 1]:
#  print(c)
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end='\t')
    print('\n')