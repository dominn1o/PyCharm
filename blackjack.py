import random
import sys

player_score = 0
dealers_score = 0
buy_in = 0
bet = 0
win = None
round = 0

buy_in = int(input("How much would you like to deposit?: "))
print(f"Bought ${buy_in:,} worth of chips\n")


class Cards:
    def __init__(self, rank):
        self.rank = rank

    def __str__(self):
        return f"{self.rank}"

    def __repr__(self):
        return self.__str__()

    def value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return "A"
        else:
            return int(self.rank)


class Deck(Cards):
    def __init__(self):
        ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # Add Ace
        self.cards = [Cards(rank) for rank in ranks] * 4  # Use multiple decks (standard 4 decks)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if self.cards:  # Check if there are any cards left in the deck
            return self.cards.pop()
        else:
            print("No more cards left.")


# Initialize the deck globally
deck = Deck()
deck.shuffle()


def bets():
    global round
    global dealers_score
    global player_score
    global deck

    deck = Deck()  # Reinitialize the deck
    deck.shuffle()

    round += 1
    dealers_score = 0
    player_score = 0
    start()


def start():
    global buy_in
    global bet
    global dealers_score

    bet = int(input("How much would you like to bet?: "))
    print(f"Round {round} with ${bet:,}\n")

    dealer_first_turn()
    player()
    dealer()


def dealer_first_turn():
    global dealers_score

    card = deck.deal()
    print(f"The dealer has a {card}.")

    card_values = [card.value()]

    if card.rank == 'A':
        if dealers_score + 11 <= 21:
            card_values = 11
        else:
            card_values = 1

    dealers_score += sum(card_values)


def money(win):  # Calculate money profit, loss, total, and total_profit
    global buy_in
    global bet

    if win:
        print("Congratulations, you win")
        buy_in += bet
        print(f"You won ${bet}\n")
        print(f"Your current balance is ${buy_in}")
    else:
        buy_in -= bet
        print(f"You lost ${bet}")
        print(f"Your current balance is ${buy_in}")

    next_round()


def next_round():
    while True:
        next_round = input("Would you like to start the next round or walk away? (y/n): ")
        if next_round == "y":
            bets()
        elif next_round == "n":
            sys.exit()
        else:
            next_round = input("Input a valid option: ")


def score(player_score, *cards):
    global win

    card_values = [card.value() for card in cards]

    for card in cards:
        if card.rank == 'A':
            if player_score + 11 <= 21:
                card_values[cards.index(card)] = 11
            else:
                card_values[cards.index(card)] = 1

    player_score += sum(card_values)

    if player_score > 21:
        win = False
        print("Bust! You lose.\n")
        money(win)
    elif player_score == 21:
        win = True
        money(win)

    card_str = ", ".join(str(card) for card in cards)
    print(f"Current Score: {player_score}\n")

    return player_score


def dealer_score(dealers_score, *cards):
    global win
    global player_score

    card_values = [card.value() for card in cards]

    for card in cards:
        if card.rank == 'A':
            if dealers_score + 11 <= 21:
                card_values[cards.index(card)] = 11
            else:
                card_values[cards.index(card)] = 1

    dealers_score += sum(card_values)

    print(f"The dealer's score is {dealers_score}")

    if dealers_score > 21:  # Dealer busts
        win = True
        money(win)
    elif dealers_score >= 17 and dealers_score > player_score:  # Dealer wins if their score is higher and between 17 and 21
        win = False
        money(win)
    elif dealers_score >= 17 and dealers_score < player_score:  # Player wins if dealer stands and player's score is higher
        win = True
        money(win)
    elif dealers_score == player_score:  # Draw
        print("It's a draw!")
        next_round()
    else:
        # Dealer should draw more cards if score is less than 17
        dealers_score = dealer_score(dealers_score, deck.deal())

    card_str = ", ".join(str(card) for card in cards)
    print(f"Dealer's current Score: {dealers_score}\n")

    return dealers_score


def dealer():
    global dealers_score

    while True:
        card = deck.deal()
        print(f"The dealer's card is {card}\n")
        dealers_score = dealer_score(dealers_score, card)


def player():
    global player_score

    card1 = deck.deal()
    card2 = deck.deal()

    print(f"Your two cards are {card1} and {card2}")
    player_score = score(player_score, card1, card2)

    while True:
        hit_or_stand = input("Would you like to hit or stand? (h/s): ")
        if hit_or_stand == "h":
            card = deck.deal()
            print(f"Your new card is {card}\n")
            player_score = score(player_score, card)
        elif hit_or_stand == "s":
            print("You have ended your turn, it's the dealer's turn to draw now.")
            dealer()
            break
        else:
            print("Invalid input")


bets()
