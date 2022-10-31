N = int(input("Количество пассажиров\n"))

K = int(input("Количество ячеек\n"))

a = ['0'] * K

for i in range(N):

    visitor = input("Введите имя и вермя через пробел в формате: имя 00:00 00:00\n")

    luggage_out_min = visitor[-2:]
    luggage_out_hour = visitor[-5:-3]
    luggage_in_min = visitor[-8: -6]
    luggage_in_hour = visitor[-11: -9]
    visitor = visitor[:-12]

    for j in range(K):
        if int(a[j][0:2]) < int(luggage_in_hour) or \
                (int(a[j][0:2]) == int(luggage_in_hour) and int(a[j][3:5]) <= int(luggage_in_min)):
            a[j] = luggage_out_hour + ':' + luggage_out_min
            print(visitor + ' ' + str(j + 1))
            break