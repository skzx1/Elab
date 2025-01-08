'''Write a program that gets an integer until user inputs a negative value.

Report the amount of odd numbers received (excluding the negative value)

Example
Enter number: 23
Enter number: 4
Enter number: 1
Enter number: 46
Enter number: 765
Enter number: 234
Enter number: -90
Received 3 odd numbers'''
c = 0
while True:
    v = int(input("Enter number: "))
    if v < 0:
        print(f"Received {c} odd numbers")
        break
    elif v % 2 == 1:
        c += 1