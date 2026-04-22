def calculator():
    check = True

    a = input("Pick your first number: ")
    b = input("Pick your second number: ")

    if a.isdigit():
        number1 = int(a)
    else:
        while check:
            a = input("Please input valid first number: ")
            if a.isdigit() == True:
                check = False
        number1 = int(a)

    check = True

    if b.isdigit():
        number2 = int(b)
    else:
        while check:
            b = input("Please input valid second number: ")
            if b.isdigit() == True:
                check = False
        number2 = int(b)

    check = True

    print("Your first number is %d" %number1)
    print("Your second number is %d" %number2)


    print("What operation would you like to do with those numbers?")
    print("Type '+' for addition, '-' for subtraction, '*' for multiplication or '/' for division:")
    while check:
        operation = input("Please input valid operation: ")
        if operation == '+':
            check = False
        if operation == '-':
            check = False
        if operation == '*':
            check = False
        if operation == '/':
            check = False

    check = True

    if operation == '+':
        print("The result is ", str((number1 + number2)))
    elif operation == '-':
        print("The result is ", str((number1 - number2)))
    elif operation == '*':
        print("The result is ", str((number1 * number2)))
    elif operation == '/':
        result = (number1 // number2)
        remainder = number1 % number2
        if (remainder != 0):
            print("The result is {0} and the remainder is {1}".format(result, remainder))
        else:
            print("The result is %d" %result)


    restart = input("Would you like to perform another calculation? (y/n): ")
    if restart == 'y':
        calculator()
    else:
        return 0
calculator()