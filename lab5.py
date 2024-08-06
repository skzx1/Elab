height = int(input("Enter height: "))
s = 3
i = 1

while height > 0:
    if i == 1:
        print(" " * (2 * (height - 1)) + "1")
    else:
        print(" " * (2 * (height - 1)) + "1" + " " * s + "1")
        s += 4
    height -= 1    
    i += 1