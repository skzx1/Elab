num = int(input(""))
re = 1
no = -1
max = 4000000
while 0 < num:
    digit = num % 10
    if digit % 2 == 0:
        re *= digit
    num //= 10 
if re ==1:
    print(no)
elif re > max:
    print("Error")
else:
    print(re)