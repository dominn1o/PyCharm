message = 'jebac kurwy'
k = 2342

def thousandCaesarCipher( message, k ):
    messageList = []
    messageEncoded = []
    for i in message:
        messageList.append(i)
    print(messageList)

    for i in messageList:
        if i == ' ':
            messageEncoded.append(' ')
        else:
            temp = k
            while temp > 0:
                next = ord(i) + temp
                if next > 122:
                    next = 97
                temp-=1
            messageEncoded.append(chr(next))
    print(messageEncoded)

thousandCaesarCipher(message, k)