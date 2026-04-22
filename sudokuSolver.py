# generates a random sudoku and gives the user the option to click enter to solve the sudoku using a brute force algorithm
# in tkinter
# gives user option to choose easy (n - n random empty fields), medium (2n - 2n empty fields), hard (3n - 3n empty fields)

"""
In all 9 sub matrices 3×3 the elements should be 1-9, without repetition.
In all rows there should be elements between 1-9 , without repetition.
In all columns there should be elements between 1-9 , without repetition.

Randomly take any number 1-9.
Check if it is safe to put in the cell.(row , column and box)
If safe, place it and increment to next location and go to step 1.
If not safe, then without incrementing go to step 1.
Once matrix is fully filled, remove k no. of elements randomly to complete game.
"""
import random

sudoku = [[0 for i in range(9)] for j in range(9)]


# checker functions check if the placement is valid, if not return 0 and generate another number in fillCell()
def checkRow(sudoku):

    return 1

def checkColumn(sudoku):
    return 1

def checkBox(sudoku):
    return 1

def fillCell():
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if sudoku[i][j] != "|":
                sudoku[i][j] = random.randint(1, 9)
            while checkRow(sudoku) == 0 or checkColumn(sudoku) == 0 or checkBox(sudoku) == 0:
                sudoku[i][j] = random.randint(1, 9)
            print(sudoku[i][j])
        print("\n")

fillCell()

for i in sudoku:
    print(i)
"""
def generate_grid(grid_data):
    rows = len(grid_data)
    cols = len(grid_data[0])

    # Determine the width of each column based on the longest number in each column
    col_widths = [max(len(str(grid_data[row][col])) for row in range(rows)) for col in range(cols)]

    # Function to create a horizontal separator between rows
    def create_separator():
        sep = '+'
        for col in range(cols):
            sep += '-' * (col_widths[col] + 2)  # Add column width + padding
            if (col + 1) % 3 == 0 and col != cols - 1:  # Add a "+" every 3 columns, except at the last column
                sep += '+'
        return sep + '+'

    # Create grid
    for row in range(rows):
        if row % 3 == 0:  # Create a bold separator every 3 rows (for Sudoku-like sections)
            print(create_separator())

        # Create the row with numbers and vertical lines every 3 columns
        row_str = '|'
        for col in range(cols):
            cell_value = str(grid_data[row][col])
            # Pad cell content based on column width
            row_str += ' ' + cell_value.center(col_widths[col]) + ' '
            if (col + 1) % 3 == 0:  # Add a "|" after every 3 numbers, but not at the last column
                row_str += '|'
        print(row_str)

    # Print the final horizontal separator at the bottom
    print(create_separator())

generate_grid(sudoku)
"""