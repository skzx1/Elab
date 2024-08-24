num1 = int(input("Enter a number: "))
num2 = int(input("Enter a digit: "))
x = 0

if num1 < 0:
    print("Invalid number.")

if num2 > 9 or num2 < 0:
    print("Invalid digit.")

if num1 >= 0 and 0 <= num2 <= 9:
     while num1 > 0:
         digit = num1 % 10
         if digit == num2:
             x += 1
         num1 //= 10
     if x == 1:
       print(f"Digit {num2} occurs {x} time.")
     else:
       print(f"Digit {num2} occurs {x} times.")
    