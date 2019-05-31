
x = 0
y = 0
z = 0

booll = True
interation = 0

while booll == True:
    interation = interation + 1


    if x * y == 20 and x + y == 12:
        print(" ")
        print("antwoord X", x)
        print("antwoord Y", y)
        print(" ")
        print("Interations =", interation)

        booll = False

    else:
        x = x +0.01
        x = round(x, 2)

        if x == 100:
            y = y + 0.01
            y = round(y,2)
            if y % 1 == 0:
                print("Bezig Y,", y)
            x = 0

