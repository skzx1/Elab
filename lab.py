hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))
if hours < 0 or hours > 20 or minutes < 0 or minutes > 59  or (hours == 20 and minutes > 0):
    print(“Invalid time.”)
else:
    if minutes > 0:
        hours += 1
    if buyAmt >= 3001:
        print(“No charge, thank you.”)
    elif buyAmt >= 300:
        if hours <= 4:
            print(“No charge, thank you.”)
        else:
            charge = (hours - 4) * 50
            print(f”Total amount due is {charge} Baht, thank you.”)
    else:
        if hours <= 2:
            print(“No charge, thank you.”)
        else:
            if hours <= 4:
                charge = (hours - 2) * 20
            else:
                charge = 2 * 20 + (hours - 4) * 50
            print(f”Total amount due is {charge} Baht, thank you.”)
