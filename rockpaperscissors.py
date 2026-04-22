import random

def rockpaperscissors():
    moves = ["rock", "paper", "scissors"]
    computer = random.choice(moves)

    player = False

    while player == False:
        player= input("rock, paper or scissors: ")
        if player.lower() == computer:
            print("computer: " + computer)
            print("Tie!")
        elif player.lower() == 'rock':
            if computer == 'scissors':
                print("computer: " + computer)
                print("You win!")
            elif computer == 'paper':
                print("computer: " + computer)
                print("You lose!")
        elif player.lower() == 'paper':
            if computer == 'rock':
                print("computer: " + computer)
                print('You win!')
            elif computer == 'scissors':
                print("computer: " + computer)
                print("You lose!")
        elif player.lower() == 'scissors':
            if computer == 'paper':
                print("computer: " + computer)
                print('You win!')
            elif computer == 'rock':
                print("computer: " + computer)
                print('You lose!')
        else:
            print("This is not a valid play.")
        player = False
        break
    restart = input("Would you like to play again? (y/n): ")
    if restart == 'y':
        rockpaperscissors()

rockpaperscissors()