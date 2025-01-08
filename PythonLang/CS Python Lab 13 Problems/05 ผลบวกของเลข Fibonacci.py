'''ผลบวกของเลข Fibonacci
เลข Fibonacci F(n) มีนิยามดังนี้

F(0) = 1

F(1) = 1

F(2) = F(0) + F(1) = 2

F(3) = F(1) + F(2) = 3

.

.

F(n) = F(n-2) + F(n-1)

ดังนั้นลำดับ Fibonacci เมื่อ n เป็น 6 จึงมีค่าดังนี้ 1, 1, 2, 3, 5, 8, 13

ให้นิสิตเขียนโปรแกรมรับค่า n และตัวอักษร 1 ตัว จากนั้นให้สร้างลำดับ Fibonacci ตั้งแต่ F(0) ถึง F(n) และคำนวณผลรวมของลำดับ Fibonacci ตามตัวอักษรนั้น นั่นคือ

ถ้าตัวอักษรเป็น "e" หรือ "E" ให้แสดงผลบวกของ F(i) เมื่อ 0 <= i <= n และ i เป็นเลขคู่
ถ้าตัวอักษรเป็น "o" หรือ "O" ให้แสดงผลบวกของ F(i) เมื่อ 0 <= i <= n และ i เป็นเลขคี่
เช่น เมื่อ n=6 และตัวอักษรเป็น e เราจะแสดงค่าของ F(0)+F(2)+F(4)+F(6) = 1+2+5+13 =21

ถ้าข้อมูลเข้าผิดพลาดให้พิมพ์คำว่า "ERROR" แล้วจบการทำงาน

ตัวอย่างข้อมูลเข้า/ข้อมูลออก

ข้อมูลเข้า	ข้อมูลออก
6
e	       21
5
O	       12
ตัวอย่าง
6
e
21
ตัวอย่าง 2
5
O
12

'''
n = int(input())
word = input()
Func1 = 'Ee'
Func2 = 'Oo'

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
if n < 0 or word not in Func1 and word not in Func2 or n == 0 and word in Func2:
    print('ERROR')
else:
    if n == 0:
        print(1)
    else:
        if word in Func1:
            asw1 = []
            for i in range(n+1):
                if i % 2 == 0:
                    asw1.append(fibonacci(i))
            print(sum(asw1))
        elif word in Func2:
            asw2 = []
            for i in range(n+1):
                if i % 2 != 0:
                    asw2.append(fibonacci(i))
            print(sum(asw2))
            