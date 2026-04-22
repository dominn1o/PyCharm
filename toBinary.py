def toBinary( number ):
    result = ''
    while number>0:
        reszta = number%2
        result += str(reszta)
        number = number//2
    return result[::-1]