x = int(input(""))
n = int(input(""))
if x < 1 or x > 7 or n < 1 or n > 31:
    print("ERROR")
else:
    day = (n - x) % 7
    if day == 0:
        print("Sunday")
    elif day == 1:
        print("Monday")
    elif day == 2:
        print("Tuesday")
    elif day == 3:
        print("Wednesday")
    elif day == 4:
        print("Thursday")
    elif day == 5:
        print("Friday")
    elif day == 6:
        print("Saturday")