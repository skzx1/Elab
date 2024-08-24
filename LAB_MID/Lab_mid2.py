num = int(input("Please input number: "))
count = 0
i = 0   
if num > 0:
    print(num)
    while num > i:
        if num % 2 == 0:
            num //= 2
            print(num)
            count += 1
        elif num % 2 == 1:
            num -=1
            print(num)
            count += 1
        while num == 0:
            if count > 1:
                print(f"{count:.0f} steps")
            else:
                print(f"{count:.0f} step")
            break
else:
    print("Error")