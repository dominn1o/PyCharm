def toDecimal(number, system):
    result = 0
    revNumber = number[::-1]
    for index, char in enumerate(revNumber):
        digit = int(char)
        result+=digit*system**index
    return result
print(toDecimal('121', 9))

def toAnything(number, system):
    results = ''
    while number > 0:
        reszta = number%system
        results += str(reszta)
        number = number//system
    return results[::-1]
print(toAnything(384, 3))
