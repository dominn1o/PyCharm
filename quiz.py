questions = {
    "skibidi: " : "A",
    "siala baba mak?: " : "C",
    "wiedziala jak?: " : "B",
    "nettspend sigma?: " : "C"
}

optons = [["A. toaleta", "B. zmywarka", "C. pralka", "D. chuj"],
         ["A. nie", "B. nwm", "C. tak", "D. chuj"],
         ["A. moze morze", "B. chb ta", "C. nah", "D. chuj"],
         ["A. LLLLLLLLLL", "B. kurwa kto", "C. fyeeeeee", "D. chuj"]]


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for  key in questions:
        print("")
        print(key)
        for i in optons[question_num - 1]:
            print(i)

        guess = input("Enter (A. B, C, D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("yessir sigma z cb")
        return 1
    else:
        print("fuj -100 aury")
        return 0


def display_score(correct_guesses, guesses):
    print("")
    print("WYNIKI")
    print("")
    print("Odp: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("tw opd: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("tw wynik jo : " + str(score) + "%")

def play_again():
    again = input("grasz znowu ni badz pizdeczka (ta/na): ")
    if again == "ta":
        return True
    else:
        return False


new_game()
while play_again():
    new_game()

print("elo miekka faja pozdro z fartem rucham tb matke")
