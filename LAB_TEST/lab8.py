c = int(input(""))
a = 1
count = 0
while a < c:
    b = a
    while b < c:
        if a * a + b * b == c * c:
            count += 1
        b += 1
    a += 1
print(count)