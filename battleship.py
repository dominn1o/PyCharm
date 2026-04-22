from random import randint
import sys

check = True
targets = input("How many targets would you like to try? \nFor every target you get 5 turns, and the board gets 3x3 times bigger \n(default: 1 target, 5 turns, 5x5 board): ")
if targets == "":
    targets = 1
targets = int(targets)
turns = targets*5
board_rows = targets*3
board_cols = targets*3


def game():
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        sys.exit()
    else:
        if (guess_row < 0 or guess_row > board_rows - 1) or (guess_col < 0 or guess_col > board_cols - 1):
            print("Oops, that's not even in the ocean.")
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    # Print (turn + 1) here!
        print_board(board)
    if turn == turns:
        print("Game Over")
        print("The ship was at row {}, column {}".format(ship_row, ship_col))

#board generation
board = []
if targets == 1:
    board_cols = 5
    board_rows = 5
    for x in range(5):
        board.append(["O"] * 5)
else:
    for x in range(targets*3):
        board.append(["O"] * (targets*3))

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

#ship generation
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#print (ship_row)
#print (ship_col)

#row and column guesses inputs
if targets == 1:
    for turn in range(5):
      print("Turn " + str(turn + 1) + " out of 5")
      guess_row = input("Guess Row: ")
      while check:
        if guess_row.isdigit() == True:
            check = False
        else:
            guess_row = input("Enter valid row: ")
      guess_row = int(guess_row)

      check = True

      guess_col = input("Guess Col: ")
      while check:
          if guess_col.isdigit() == True:
              check = False
          else:
              guess_col = input("Enter valid column: ")
      guess_col = int(guess_col)

      check = True

      game()
else:
    for turn in range(turns):
        print("Turn " + str(turn + 1) + " out of " + str(turns))
        guess_row = input("Guess Row: ")
        while check:
            if guess_row.isdigit() == True:
                check = False
            else:
                guess_row = input("Enter valid row: ")
        guess_row = int(guess_row)

        check = True

        guess_col = input("Guess Col: ")
        while check:
            if guess_col.isdigit() == True:
                check = False
            else:
                guess_col = input("Enter valid column: ")
        guess_col = int(guess_col)

        check = True
        game()


