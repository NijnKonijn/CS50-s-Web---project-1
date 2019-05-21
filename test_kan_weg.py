no_first_line = True
x = 0
while x < 3:
    if no_first_line is True:  # skip first line
        no_first_line = False
        print("you skipped the first line")
    if no_first_line is False:
        print(x)
        x = x + 1