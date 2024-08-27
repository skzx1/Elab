first = int(input(""))
second = int(input(""))
firstplay = first + second
count = 1
if firstplay == 7  or firstplay == 11:
    print("W")
elif firstplay == 2 or firstplay == 3 or firstplay == 12:
    print("L")
elif firstplay == 4 or firstplay == 5 or firstplay == 6 or firstplay == 8 or firstplay == 9 or firstplay == 10:
    target = firstplay
    while True:
        first = int(input(""))
        second = int(input(""))
        secondplay = first + second
        final = first + second
        count += 1
        if first < 1 or first > 9:
            print("Error")
            count == count 
        elif second < 1 or second > 9:
            print("Error")
            count == count 
        elif secondplay == target:
            print(f"{count} {final} W")
            break
        elif secondplay == 7:
            print(f"{count} L")
            break
        

