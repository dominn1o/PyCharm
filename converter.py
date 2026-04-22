units = ['g', 'oz', 'kg', 'lbs', 'ml', 'cups', 'l', 'gal', 'cm', 'in', 'm', 'ft', 'c', 'fh', 'km', 'mi']
pairs = {'g' : 'oz',
         'kg' : 'lbs',
         'ml' : 'cups',
         'l' : 'gal',
         'cm' : 'in',
         'm' : 'ft',
         'c' : 'fh',
         'km' : 'mi',
         }

g_to_oz = 0.035274
oz_to_g = 28.3495
kg_to_lbs = 2.20462
lbs_to_kg = 0.453592
ml_to_cups = 0.00422675
cups_to_ml = 240
l_to_gal = 0.264172
gal_to_l = 3.78541
cm_to_in = 0.393701
in_to_cm = 2.54
m_to_ft = 3.28084
ft_to_m = 0.3048
c_to_fh = 9/5
fh_to_c = 5/9
km_to_mi = 0.621371
mi_to_km = 1.60934


def converter():

    check = True
    check2 = True
    check3 = True

    print("Pick the unit you want to convert: ")
    unit1 = input("(g - oz); (kg - lbs); (ml - cups); (l - gal); (cm - in); (m - ft); (c - fh); (km - mi): ")

    while check:
        if unit1 not in units:
            unit1 = input("Enter valid unit: ")
        else:
            check = False

    check = True

    print("Pick the unit you want to convert to: ")
    unit2 = input("(g - oz); (kg - lbs); (ml - cups); (kg - gal); (cm - in); (m - ft); (c - fh); (km - mi): ")

    while check:
        if unit2 not in units:
            unit2 = input("Enter valid unit: ")
        else:
            check = False

    check = True

    amount = input("Input the amount of the unit of measurement: ")

    while check:
        if amount.isdigit() == True:
            check = False
        else:
            amount = input("Enter valid amount: ")

    amount = float(amount)

    check = True

    for key, value in pairs.items():
        if (unit1 == key and unit2 == value) or (unit1 == value and unit2 == key):
            check = False
            break

    while check3:
        if check == False:
            print("Your selected units are %s and %s" %(unit1, unit2))
            break
        else:
            print("Your selected inputs don't match any pairs, please select again.")

            print("Pick the unit you want to convert: ")
            unit1 = input("(g - oz); (kg - lbs); (ml - cups); (l - gal); (cm - in); (m - ft); (c - fh); (km - mi): ")

            while check2:
                if unit1 not in units:
                    unit1 = input("Enter valid unit: ")
                else:
                    check2 = False

            check2 = True

            print("Pick the unit you want to convert to: ")
            unit2 = input("(g - oz); (kg - lbs); (ml - cups); (kg - gal); (cm - in); (m - ft); (c - fh); (km - mi): ")

            while check2:
                if unit2 not in units:
                    unit2 = input("Enter valid unit: ")
                else:
                    check2 = False

            check2 = True

            for key, value in pairs.items():
                if (unit1 == key and unit2 == value) or (unit1 == value and unit2 == key):
                    check = False
                    break

            if check == False:
                print("Your selected units are %s and %s" % (unit1, unit2))
                check3 = False

    check = True
    check3 = True

    if unit1 == 'g':
        if unit2 == 'oz':
            conversion = amount*g_to_oz
            print(str(amount) + " grams are equal to " + str(conversion) + " ounces.")

    if unit1 == 'oz':
        if unit2 == 'g':
            conversion = amount*oz_to_g
            print(str(amount) + " ounces are equal to " + str(conversion) + " grams.")

    if unit1 == 'kg':
        if unit2 == 'lbs':
            conversion = amount*kg_to_lbs
            print(str(amount) + " kilograms are equal to " + str(conversion) + " pounds.")

    if unit1 == 'lbs':
        if unit2 == 'kg':
            conversion = amount*lbs_to_kg
            print(str(amount) + " pounds are equal to " + str(conversion) + " kilograms.")

    if unit1 == 'ml':
        if unit2 == 'cups':
            conversion = amount*ml_to_cups
            print(str(amount) + " mililitres are equal to " + str(conversion) + " cups.")

    if unit1 == 'cups':
        if unit2 == 'ml':
            conversion = amount*cups_to_ml
            print(str(amount) + " cups are equal to " + str(conversion) + " mililitres.")

    if unit1 == 'l':
        if unit2 == 'gal':
            conversion = amount*l_to_gal
            print(str(amount) + " litres are equal to " + str(conversion) + " gallons.")

    if unit1 == 'gal':
        if unit2 == 'l':
            conversion = amount*gal_to_l
            print(str(amount) + " gallons are equal to " + str(conversion) + " litres.")

    if unit1 == 'cm':
        if unit2 == 'in':
            conversion = amount*cm_to_in
            print(str(amount) + " centimetres are equal to " + str(conversion) + " inches.")

    if unit1 == 'in':
        if unit2 == 'cm':
            conversion = amount*in_to_cm
            print(str(amount) + " inches are equal to " + str(conversion) + " centimetres.")

    if unit1 == 'm':
        if unit2 == 'ft':
            conversion = amount*m_to_ft
            print(str(amount) + " metres are equal to " + str(conversion) + " feet.")

    if unit1 == 'ft':
        if unit2 == 'm':
            conversion = amount*ft_to_m
            print(str(amount) + " feet are equal to " + str(conversion) + " metres.")

    if unit1 == 'c':
        if unit2 == 'fh':
            conversion = amount*c_to_fh+32
            print(str(amount) + " degrees celsius is equal to " + str(conversion) + " degrees farenheit.")

    if unit1 == 'fh':
        if unit2 == 'c':
            conversion = (amount-32)*fh_to_c
            print(str(amount) + " degrees farenheit is equal to " + str(conversion) + " degrees celsius.")

    if unit1 == 'km':
        if unit2 == 'mi':
            conversion = amount*km_to_mi
            print(str(amount) + " kilometres are equal to " + str(conversion) + " miles.")

    if unit1 == 'mi':
        if unit2 == 'km':
            conversion = amount*fh_to_c
            print(str(amount) + " miles are equal to " + str(conversion) + " kilometres.")


    restart = input("Would you like to perform another conversion? (y/n): ")
    if restart == 'y':
        converter()
    else:
        return 0



converter()