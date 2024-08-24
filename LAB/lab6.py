n = int(input(""))
i = 1
min = n + 1
while i <= n // 2:
    if n % i == 0:
        sum = i + n // i
        if sum < min:
          min = sum
    i += 1
print(min)
