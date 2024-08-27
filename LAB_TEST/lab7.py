while True:
  x = int(input("Enter a number: "))
  if x == 0:
    print("End of program, goodbye.")
    break
  elif x <= 1:
    print("Invalid input, try again.")  
  else:
    i = 2
    prime = True
    while i <= x // i:
       if x % i == 0:
        prime = False
       i += 1
    if prime:
      print(x, "is a prime number.")
    else:
      print(x, "is not a prime number.")
      
  