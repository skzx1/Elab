target = int(input("Enter a target (4-digit integer): "))
ans = int(input("Enter your guess (4-digit integer): "))
pos = 0 
count = 0
i1 = 0
i2 = 0
while True:
    if (target == ans):
        print("Congratulations, you just mastered my mind!!")
        break
    y = target
    while True:
        if (y == 0):
            y = target
            ans //= 10
            i2 = 0
            i1 += 1
        elif (ans == 0):
            break
        if (y % 10 == ans % 10 and i2 == i1):
            pos += 1
        elif (y % 10 == ans % 10):
            count += 1
        y //= 10
        i2 += 1
    if pos == 0:
        pos = "No"
    elif pos == 1:
        pos = "One"
    elif pos == 2:
        pos = "Two"
    elif pos == 3:
        pos = "Three"
    
    if count == 0:
        count = "no"
    elif count == 1:
        count = "one"
    elif count == 2:
        count = "two"
    elif count == 3:
        count = "three"
    elif count == 4:
        count = "four"


    if (pos == "No" and count == "No"):
        print("No positions correct, no digits correct")
    elif (pos == "One" and count == 'one'):
        print(f"{pos} position correct, {count} digit correct")
    elif (pos == 'One'):
        print(f"{pos} position correct, {count} digits correct")
    elif (count == 'one'):
        print(f"{pos} positions correct, {count} digit correct")
    elif (pos == "No" and count != "one"):
        print(f'No positions correct, {count} digits correct')
    elif (count == "no" and pos != "One"):
        print(f"{pos} positions correct, no digits correct")
    else:
        print(f"{pos} positions correct, {count} digits correct")
    break
