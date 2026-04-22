import random

lenght = int(input("How long would you like your password to be (characters)?: "))
special_char = input("Would you like to include special characters? (y/n): ")
password = ""

chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

    # Letters (Lowercase)
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

    # Digits
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Punctuation and Symbols
special_chars = ['.', ',', ':', ';', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '"', '<', '>', '/', '?', '`', '~']

all_chars = chars + special_chars
if special_char == "y":
    for i in range(lenght):
        password = password + random.choice(all_chars)
elif special_char == "n":
    for i in range(lenght):
        password = password + random.choice(chars)
else:
    print("Invalid input")

print(f"Your password is:\n{password}")