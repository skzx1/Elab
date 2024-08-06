hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))
tcost = 0
if hours < 0 or hours >= 20 or minutes < 0 or minutes >= 60:
    print("Invalid time.")
else:
        if minutes > 0:
            thours = hours + 1
        else:
            thours = hours
        if buyAmt >= 3001 or thours <= 2:
             print("No charge, thanks.")
        else:
            if buyAmt >= 300:
                free = 4
            else:
                free = 2
            if thours <= free:
                tcost = 0
            elif thours <= 4:
                tcost = (thours - free) * 20
            else:
                tcost = (4 - free) * 20 + (thours - 4) * 50
        
            print(f"Total amount due is {tcost} Bahts, thank you.")
