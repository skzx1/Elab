'''จงเขียนฟังก์ชันชื่อ check_prime(n) โดยรับค่า n จากโปรแกรมหลักเพื่อตรวจสอบว่าค่า n นั้นเป็นจำนวนเฉพาะหรือไม่

ให้ฟังก์ชันดังกล่าวคืนค่าเป็นบูล (นั่นคือ คืนค่า True ถ้าเป็นจำนวนเฉพาะ และคืนค่า False ถ้าไม่ใช่)'''
def check_prime(n):
    i = 2
    x = True
    while  i <= n/2:
        if n % i == 0:    
            x = False
            break
        i+=1  
    return x
'''
[hide line #]
ตัวอย่างของโปรแกรมหลักที่เรียกใช้ฟังก์ชันดังกล่าวคือ


[hide line #]
n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")
ตัวอย่างการเรียกใช้งานผ่านโปรแกรมหลักแสดงด้านล่าง

Example 1
Enter number: 100
100 is not a prime number.
Example 2
Enter number: 139
139 is a prime number.'''
