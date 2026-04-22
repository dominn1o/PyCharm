import random
import sys

play = input("How many players? (The default is 2): ")
if not play:
    play = 2
elif play.isdigit() == False:
    while True:
        play = input("Enter valid number: ")
        if play.isdigit() == True:
            break
play = int(play)

players = []
for i in range(play):
    players.append(f"player{i + 1}")

total_score1 = 0
total_score2 = 0



class Scores:     #display total score
    def __init__(self):
        self.scores = {}
        for item in players:
            self.scores[item] = 0

    def total_score(self, player, result):
        if player in self.scores:
            self.scores[player] += result
    def reset_score(self, player, result):
        if result == 1:
            self.scores[player] *= 0

game_scores = Scores()

def turn(player, goal):   #loop to roll dice, check if dice is one or not, add score to game_score
    while True:
        if game_scores.scores[player] >= goal:
            print(f"{player.capitalize()} wins!")
            sys.exit()
        else:
            pass
        roll = input("Press enter to roll dice, type anything to end your turn: ")
        if roll == "":
            result = random.randint(1, 6)
        else:
            print("You have ended your turn")
            print(f"{player.capitalize()}'s total score: {game_scores.scores[player]}")
            break

        if result == 1:
            print("Unlucky, you reset your score!\n")
            game_scores.reset_score(player, result)
        else:
            print("You added {} to your total score\n".format(result))
            game_scores.total_score(player, result)




def switch_turns(players, goal):   #when condition is met on turn(), alternate to next player
    while True:
        for player in players:
            print("\n{}'s turn!\n".format(player))
            turn(player, goal)


def game(players):
    print("\nWelcome to the game of pig. The rules are: \nEach player gets a turn during which they can roll dice as many times as they want.\nIf the dice lands on any number other than 1, it gets added to their score.")
    print("However if the dice does land on 1 the players total score gets reset to 0.\nYou can also decide to stop your current turn if you don't want to risk it.")
    print("The first person to reach a set score wins\n")
    goal = input("What score would you like to play up to? (The default is 50): ")
    if not goal:
        goal = 50
    elif goal.isdigit() == False:
        while True:
            goal = input("Enter valid number: ")
            if goal.isdigit() == True:
                break
    goal = int(goal)

    switch_turns(players, goal)

game(players)
