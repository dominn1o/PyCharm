import pyautogui

chooseAnswer = [512, 681]
secondAnswer = [508, 763]
Answer = [813,686]
Continue = [423,685]

while True:

    #every ten answers click continue
    counter = 0
    print(counter)

    # move to choose answer and click
    pyautogui.moveTo(chooseAnswer[0], chooseAnswer[1], duration=1)
    pyautogui.click(chooseAnswer[0], chooseAnswer[1])

    #move to the second option and click
    pyautogui.moveTo(secondAnswer[0], secondAnswer[1], duration=1)
    pyautogui.click(secondAnswer[0], secondAnswer[1])

    #Move to the answer button and click
    pyautogui.moveTo(Answer[0], Answer[1], duration=1)
    pyautogui.click(Answer[0], Answer[1])

    # every ten answers click continue
    if counter%10 == 0 and counter/10 > 0:
        pyautogui.moveTo(Continue[0], Continue[1], duration=1)
        pyautogui.click(Continue[0], Continue[1])



