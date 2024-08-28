'''หลักเลข
จงเขียนโปรแกรมเพื่อรับจำนวนเต็ม num ที่กำหนดให้มีค่าตั้งแต่ 0 และน้อยกว่า 10,000 สร้างฟังก์ชันเพื่อส่งกลับตัวเลข ของแต่ละหลักดังนี้

digit(num) เพื่อคืนค่าตัวเลขในหลักหน่วยของจำนวนเต็ม num
tens(num) เพื่อคืนค่าตัวเลขในหลักสิบของจำนวนเต็ม num
hundreds(num) เพื่อคืนค่าตัวเลขในหลักร้อยของจำนวนเต็ม num
thousands(num) เพื่อคืนค่าตัวเลขในหลักพันของจำนวนเต็ม num
นอกจากนี้ให้สร้างฟังก์ชัน sum_digits(num) เพิ่มเติมเพื่อคืนค่าผลบวกของตัวเลขในแต่ละหลักของ num

ตัวอย่าง Input/Output
Enter a number (0 to 9999): 8143
Digit place is 3.
Tens place is 4.
Hundreds place is 1.
Thousands place is 8.
Sum of all digits is 16.'''
def digit(n):
    num = n % 10
    return num
def tens(n):
    n //= 10
    num = n % 10
    return num
def hundreds(n):
    n //= 100
    num = n % 10    
    return num
def thousands(n):
    n //= 1000
    num = n % 10       
    return num
def sum_digits(n):
    num2 = 0 
    while n > 0:
        num2 += n%10
        n //= 10
    return num2

n   = int(input('Enter a number (0 to 9999): '))
print(f'Digit place is {digit(n)}.')
print(f'Tens place is {tens(n)}.')
print(f'Hundreds place is {hundreds(n)}.')
print(f'Thousands place is {thousands(n)}.')
print(f'Sum of all digits is {sum_digits(n)}.')