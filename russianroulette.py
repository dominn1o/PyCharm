import random

def russianroulette():
    check = True
    chambers = input("Input anount of chambers, the default is 6: ")
    if not chambers:
        chambers = 6
    elif chambers.isdigit() == False:
        while check:
            chambers = input("Input valid number of chambers: ")
            if chambers.isdigit() == True:
                check = False
    chambers = int(chambers)

    check = True

    bullets = input("Input anount of bullets, the default is 1: ")
    if not bullets:
        bullets = 1
    elif bullets.isdigit() == False:
        while check:
            bullets = input("Input valid number of bullets: ")
            if bullets.isdigit() == True:
                check = False
    bullets = int(bullets)

    check = True

    if bullets > chambers:
        bullets = chambers
    else:
        pass

    bullets_list = []

    for i in range(bullets):
        while True:
            fatal_bullet = random.randint(1, chambers)
            if fatal_bullet not in bullets_list:
                bullets_list.append(fatal_bullet)
                break

    print(bullets_list)

    for i in range(1, chambers + 1):
        input("Press enter to pull the trigger: ")
        if i in bullets_list:
            print("gg ez noob kys")
            restart = input("Do you want to start again? (y/n): ")
            if restart == 'y':
                russianroulette()
            else:
                break
        print("sigma")

    check = True


russianroulette()