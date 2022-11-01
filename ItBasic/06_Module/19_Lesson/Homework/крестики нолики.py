print('*' * 10, " Крестики-нолики v.1.0", '*' * 10)

board = list(range(1, 10))


def draw_board(board):  # создаем функцию для игрового поля
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')  # создаем 9 ячеек для игры
        print('-' * 13)


def take_input(player_token):  # функция принимает ввод пользоваетля
    valid = False
    while not valid:
        player_answer = input("Куда поставим:" + player_token + "?")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if str(board[
                       player_answer - 1]) not in "X0":  # Проверка когда клетка занята или введино число не из диапазона от 1 до 9
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята")
        else:
            print("Введите число то 1 до 9")


def check_win(board):  # функция проверяет выиграл ли игрок
    win_cord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
                (2, 4, 6))  # зоздаем кортеж с выиграшными вариантами
    for e in win_cord:
        if board[e[0]] == board[e[1]] == board[e[2]]:
            return board[e[0]]
    return False


def main(board):  # собираем все вместе
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("0")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "Ты выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья")
            break
    draw_board(board)


main(board)
