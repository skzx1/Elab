height = int(input("Enter height: "))
if height >= 0:
    i = 0
    while i < height:
        if i == 0:
            print(" " * (height - 1) + "1")
        else:
            print(" " * (height - i - 1) + "1" + " " * (2 * i - 1) + "1")
        i += 1