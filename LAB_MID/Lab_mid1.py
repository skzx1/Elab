amount = float(input("Enter amount: "))
while True:
    com =  (input("Enter command (w for withdraw, d for deposit, e for exit): "))
    if com == "e":
        break
    elif com == "w":
        while True:
            withdraw = float(input("Enter withdraw amount: "))
            if withdraw <= 0:     
                print("Incorrect transactions!")
            elif withdraw > amount:
                print("You cannot withdraw more than the amount in your account!")
            else:
                amount -= withdraw
                print(f"Current balance = {amount:.2f}$")
                break        
    elif com == "d":
            while True:
                deposit = float(input("Enter deposit amount: "))
                if deposit <= 0:     
                    print("Incorrect transactions!")
                else:
                    amount += deposit
                    print(f"Current balance = {amount:.2f}$")
                    break
    else:
        print("Invalid Command!")
    
             