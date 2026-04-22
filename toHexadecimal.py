count = int(input())
lines = []
for i in range(count):
    lines.append(input().split(" "))
    lines[i][0] = int(lines[i][0])

print(lines)

def KelvinCelsius(temp):
    return temp - 273.15


def CelsiusKelvin(temp):
    return temp + 273.15


def CelsiusFarenheit(temp):
    farenheit = (temp * 1.8) + 32
    return farenheit


def FarenheitCelsius(temp):
    celsius = (temp - 32) * (5 / 9)
    return celsius


def KelvinFarenheit(temp):
    fahrenheit = (temp - 273.15) * 9 / 5 + 32
    return fahrenheit


def FarenheitKelvin(temp):
    kelvin = (temp - 32) * 5 / 9 + 273.15
    return kelvin


def checkTemp(temp, unit):
    if unit == "Celsius":
        kelvin = CelsiusKelvin(temp)
        if kelvin < 0:
            return False
        else:
            return True

    elif unit == "Farenheit":
        kelvin = FarenheitKelvin(temp)
        if kelvin < 0:
            return False
        else:
            return True

    else:
        if temp < 0:
            return False
        else:
            return True


for i in lines:
    if checkTemp(i[0], i[1]):
        if i[1] == "Kelvin":
            print(1)
            if i[2] == "Celsius":
                print(2)
                print(KelvinCelsius(i[0]))
            elif i[2] == "Farenheit":
                print(3)
                print(KelvinFarenheit(i[0]))
        elif i[1] == "Celsius":
            print(4)
            if i[2] == "Kelvin":
                print(5)
                print(CelsiusKelvin(i[0]))
            elif i[2] == "Farenheit":
                print(6)
                print(CelsiusFarenheit(i[0]))
        elif i[1] == "Farenheit":
            print(7)
            if i[2] == "Celsius":
                print(8)
                print(FarenheitCelsius(i[0]))
            elif i[2] == "Kelvin":
                print(9)
                print(FarenheitKelvin(i[0]))
    else:
        print("NO")
