'''Buffet
Write a program to help the buffet restaurant calculate the price for a customer.

The price for Japanese buffet is 1000 Baht, and the price for Korean buffet is 1500 Baht. If today is Wednesday, he will receive 15% discount.

Example 1
Enter your buffet choice: Korean
Is today Wednesday (yes/no)? no
Your payment is 1500.00 Baht.
Example 2
Enter your buffet choice: Japanese
Is today Wednesday (yes/no)? yes
Your payment is 850.00 Baht.
Example 3
Enter your buffet choice: Thai
Sorry, there is no Thai buffet.'''
l = input("Enter your buffet choice: ")
if l == "Korean":
    d = input("Is today Wednesday (yes/no)? ")
    x = 1500
    if d == "yes":
        xl = x - (x * 15 / 100)
        print(f"Your payment is {xl:.2f} Baht.")
    elif d == "no":
        print(f"Your payment is {x:.2f} Baht.")
elif l == "Japanese":
    d = input("Is today Wednesday (yes/no)? ")
    x = 1000
    if d == "yes":
        xl = x - (x * 15 / 100)
        print(f"Your payment is {xl:.2f} Baht.")
    elif d == "no":
        print(f"Your payment is {x:.2f} Baht.")
else:
    print(f"Sorry, there is no {l} buffet.")