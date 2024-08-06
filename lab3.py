x = int(input())
while x > 10:
    sum = 0
    while x > 0:
       sum += x % 10
       x //= 10
    x = sum
print(x)
