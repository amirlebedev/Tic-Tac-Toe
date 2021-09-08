import random


def print_board(matrix, max_size=9, nxn=3):

    column_counter = 1

    for i in range(0, max_size):
        print("[" + str(matrix[i]) + "]", end='')
        if column_counter >= nxn:
            print("")  # new line
            column_counter = 0
        column_counter += 1


def print_winner(token):
    print(token, "is the winner!")


def check_winner(matrix, max_size=9, nxn=3):

    column_counter = 0
    row_counter = 0
    streak = 0

    for token in ['X', 'O']:
        for i in range(0, max_size):  # check winning condition for columns
            if matrix[i] == token:
                streak += 1
            else:
                streak = 0

            if streak == nxn:
                print_winner(token)
                return token

        i = 0
        while i < nxn:  # check winning condition for rows
            streak = 0
            for cell in range(i, max_size, nxn):
                if matrix[cell] == token:
                    streak += 1
                else:
                    streak = 0

                if streak == nxn:
                    print_winner(token)
                    return token
            i += 1

        if matrix[0] == token and matrix[4] == token and matrix [8] == token:  # check diagonal todo make more robust
            print_winner(token)
            return token
        if matrix[6] == token and matrix[4] == token and matrix [2] == token:  # check diagonal todo make more robust
            print_winner(token)
            return token

    tie = True
    for i in matrix:
        if i != 'X' or i != 'O':
            tie = False
        else:
            print("Tie!")

    return 'none'


def player_turn(matrix, token, max_size=9):

    legal_place = 0
    while legal_place > max_size or legal_place <= 0:
        legal_place = input("Where would you like to put your " + token + ": ")

        if legal_place.isdigit():
            legal_place = int(legal_place)
            if legal_place > max_size or legal_place <= 0:
                legal_place = 0  # stay in loop
                print("That place is illegal.")
            elif matrix[legal_place - 1] == 'X' or matrix[legal_place - 1] == 'O':
                print("That place is already taken by " + matrix[legal_place-1])
                legal_place = 0  # stay in loop
        else:
            print("Illegal character.")
            legal_place = 0


    return legal_place - 1


def initialize():
    player_type_value = ''
    while player_type_value != '1' and player_type_value != '2':
        player_type_value = input("Press 1 for X, press 2 for O\n")
        if player_type_value != '1' and player_type_value != '2':
            print("Error: please select legal character.")

    if player_type_value == '1':
        player_token = 'X'
    else:
        player_token = 'O'

    print("\nYou go first. Where would you like to put your " + player_token + "?")
    return player_token


def ai_turn(matrix, max_size=9):

    place = 0
    seed_integer = 1
    while place <= 0 or place > max_size:
        place = random.randint(0, max_size - 1)
        if matrix[place] == 'X' or matrix[place] == 'O':
            place = 0
        seed_integer += 1

    return place


# main
matrix = ['1', '2', '3',
          '4', '5', '6',
          '7', '8', '9']

player_token = initialize()
if player_token == 'X':
    ai_token = 'O'
else:
    ai_token = 'X'

turn = 'player'
winner = 'none'

random.seed(random.randint(0, 10))

while winner == 'none':
    print_board(matrix, 9, 3)
    winner = check_winner(matrix, 9, 3)
    if winner != 'none':
        break

    if turn == 'player':
        turn = 'ai'
        place = player_turn(matrix, player_token, 9)
        matrix[place] = player_token
    else:
        print("AI turn:")
        turn = 'player'
        place = ai_turn(matrix, 9)
        matrix[place] = ai_token







