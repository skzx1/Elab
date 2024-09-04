def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    num = 1
    num1 = 1
    i = 3
    while i <= n:
        re = num + num1
        num = num1
        num1 = re
        i += 1
    return num1

n = int(input("Enter n: "))
print("fibo({}) = {}".format(n, Fibonacci(n)))