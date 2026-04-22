import sys
from random import randint


def check_winner(board):
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def random_move(board):
    check = True
    move = randint(0, len(board) - 1)
    while check:
        if board[move] == " ":
            board[move] = "O"
            print_board(board)
            check = False
        else:
            move = randint(0, len(board) - 1)



check = True
player_or_pc = input("Would you like to play vs a player or vs the computer? (p/c): ")
print("['0', '1', '2']\n['3', '4', '5']\n['6', '7', '8']")

def game(board):
    check = True

    if turns % 2 == 0:
        while True:
            try:
                print("Turn {}".format(turns))
                move = int(input("Player 1, enter the position you want to play (0-8): "))
                if move in range(len(board)):
                    if board[move] == ' ':
                        board[move] = "X"
                        break
                    else:
                        print("Spot already taken! Try again.")
                else:
                    print("Invalid move. Please enter a number between 0 and 8.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print_board(board)


    elif turns % 2 != 0:
        while True:
            try:
                print("Turn {}".format(turns))
                move = int(input("Player 2, enter the position you want to play (0-8): "))
                if move in range(len(board)):
                    if board[move] == ' ':
                        board[move] = "O"
                        break
                    else:
                        print("Spot already taken! Try again.")
                else:
                    print("Invalid move. Please enter a number between 0 and 8.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print_board(board)

def game_computer(board):
    check = True
    if turns % 2 == 0:
        while True:
            try:
                print("Turn {}".format(turns))
                move = int(input("Enter the position you want to play (0-8): "))
                if move in range(len(board)):
                    if board[move] == ' ':
                        board[move] = "X"
                        break
                    else:
                        print("Spot already taken! Try again.")
                else:
                    print("Invalid move. Please enter a number between 0 and 8.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print_board(board)

    else:
        random_move(board)


def print_board(board):
    for i in range(0, len(board), 3):
        print(board[i:i+3])

board = [" " for _ in range(9)]

winner = check_winner(board)



if player_or_pc == "p":
    for turns in range(9):
        game(board)
        winner = check_winner(board)
        if winner:
            print("Player {} wins!".format(winner))
            sys.exit()
        else:
            print(" ")


if player_or_pc == "c":
    for turns in range(9):
        if game_computer(board):
            random_move(board)
        winner = check_winner(board)
        if winner == "O":
            print("You Lose!")
            sys.exit()
        elif winner == "X":
            print("You Win!")
            sys.exit()
        else:
            print(" ")
