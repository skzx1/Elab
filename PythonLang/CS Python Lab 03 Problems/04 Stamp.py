'''Stamp
Write a program to calculate the number of stamps that customer gets after customer spent every 50 Bahts.

Example 1
Total Price: 35
You got: 0
Example 2
Total Price: 55.50
You got: 1 
Example 3
Total Price: 120.25
You got: 2 '''
x = float(input("Total Price: "))
s = x // 50
print(f'You got: {int(s)}')
