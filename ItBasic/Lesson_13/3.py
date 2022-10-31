N = int(input())  # вводим количество пассажиров не менее 3 и не более 1000

K = int(input())  # Количество ячеек не менее 10 но не более 1000

cells = ['0'] * K  # Информация о ячейках

for i in range(N):

    passenger = input()

    luggage_out_min = passenger[-2:]
    luggage_out_hour = passenger[-5:-3]
    luggage_in_min = passenger[-8: -6]
    luggage_in_hour = passenger[-11: -9]
    visitor = passenger[:-12]

    for j in range(K):
        if int(cells[j][0:2]) < int(luggage_in_hour) or \
                (int(cells[j][0:2]) == int(luggage_in_hour) and int(cells[j][3:5]) <= int(luggage_in_min)):
            cells[j] = luggage_out_hour + ':' + luggage_out_min
            print(visitor + ' ' + str(j + 1))
            break