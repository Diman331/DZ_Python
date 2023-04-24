# Задача 4*. (Необязательная). Создайте игру в крестики-нолики.
# Игра с ПК, выйграть не получится :D

import random

# Функция вывода игровой доски
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Функция определения маркера игрока
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Выберите Х или О: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Функция определения места хода игрока
def place_marker(board, marker, position):
    board[position] = marker

# Функция проверки на выигрышь
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))

# Функция выбора первого хода
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Игрок'

# Функция проверки места хода
def space_check(board, position):
    return board[position] == ' '

# Функция проверки на заполненность доски
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Функция запроса хода игрока
def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Выберите место хода от 1 до 9: '))
    return position

# Функция компьютерного хода
def computer_choice(board, computer_marker):
    for i in range(1, 10):
        if space_check(board, i):
            board_copy = board[:]
            place_marker(board_copy, computer_marker, i)
            if win_check(board_copy, computer_marker):
                return i
    for i in range(1, 10):
        if space_check(board, i):
            board_copy = board[:]
            place_marker(board_copy, player_marker, i)
            if win_check(board_copy, player_marker):
                return i
    if space_check(board, 5):
        return 5
    corners = [1, 3, 7, 9]
    random.shuffle(corners)
    for corner in corners:
        if space_check(board, corner):
            return corner
    edges = [2, 4, 6, 8]
    random.shuffle(edges)
    for edge in edges:
        if space_check(board, edge):
            return edge

# Функция повторной игры
def replay():
    return input('Хотите сыграть еще раз? Введите "Y" или "N": ').lower().startswith('y')

# Игровой процесс
print('Добро пожаловать в игру Крестики-нолики!')

while True:
    # Настройки игры
    the_board = [' '] * 10
    player_marker, computer_marker = player_input()
    turn = choose_first()
    print(turn + ' ходит первым.')
    game_on = True

    # Игровой цикл
    while game_on:
        if turn == 'Игрок':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player_marker, position)
            if win_check(the_board, player_marker):
                display_board(the_board)
                print('Поздравляем! Вы выиграли!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Компьютер'
        else:
            position = computer_choice(the_board, computer_marker)
            place_marker(the_board, computer_marker, position)
            if win_check(the_board, computer_marker):
                display_board(the_board)
                print('Компьютер выиграл!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'Игрок'

    if not replay():
        break