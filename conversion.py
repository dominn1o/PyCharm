import sys

conversion = {
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F"
}

def binary(num):
    mod = num
    mod_list = []

    if mod == 0:
        print("Your number in binary is " + str(0))
        sys.exit()

    elif mod == 1:
        print("Your number in binary is " + str(1))
        sys.exit()

    while mod != 0:
        mod_list.append(mod % 2)
        mod = mod // 2
       #print(mod)
       #print(mod_list)

    n = len(mod_list)

    binary = "".join(map(str, mod_list))
    binary = int(binary[::-1])


    print("Your number in binary is {}".format(binary))


def hexadecimal(num):
    mod = num
    mod_list = []

    if mod == 0:
        print("Your number in hexadecimal is " + str(0))
        sys.exit()

    while mod != 0:
        mod_list.append(mod % 16)
        mod = mod // 16
       #print(mod)
       #print(mod_list)

    n = len(mod_list)
    mod_list = [str(i) for i in mod_list]

    for i in range(len(mod_list)):
        if mod_list[i] in conversion:
            mod_list[i] = conversion[mod_list[i]]

    mod_list.reverse()

    hex = "".join(map(str, mod_list))

    print("Your number in hexadecimal is {}".format(hex))


def octal(num):
    mod = num
    mod_list = []

    if mod == 0:
        print("Your number in octal is " + str(0))
        sys.exit()

    while mod != 0:
        mod_list.append(mod % 8)
        mod = mod // 8
    #print(mod)
    #print(mod_list)

    mod_list.reverse()
    oct = "".join(map(str, mod_list))
    print("Your number in octal is {}".format(oct))


a = input("Would you like to convert your decimal number to binary, hexadecimal or octal? (b/h/o) : ")
if a.lower() == "b":
    num = input("What number would you like to convert to binary?: ")
    binary(int(num))
elif a.lower() == "h":
    num = input("What number would you like to convert to hexadecimal?: ")
    hexadecimal(int(num))
elif a.lower() == "o":
    num = input("What number would you like to convert to octal?: ")
    octal(int(num))