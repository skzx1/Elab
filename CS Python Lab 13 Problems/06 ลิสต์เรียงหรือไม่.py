'''ลิสต์เรียงหรือไม่
จงเขียนโปรแกรมเพื่อรับจำนวนเต็มใดๆ ที่มีค่าตั้งแต่ 0 ถึง 100 มาสร้างเป็น list โดยให้รับเข้ามาเรื่อยๆ จนผู้ใช้ใส่ -1 จึงหยุด จากนั้นให้ตรวจสอบลำดับของสมาชิกใน list และแสดงผลอย่างใดอย่างหนึ่งดังต่อไปนี้ คือ
1) สมาชิกใน list เรียงลำดับแบบ non-increasing order นั่นคือ สมาชิกมีค่าไม่เพิ่มขึ้นจากสมาชิกในลำดับก่อนหน้า
2) สมาชิกใน list เรียงลำดับแบบ non-decreasing order นั่นคือ สมาชิกมีค่าไม่ลดลงจากสมาชิกในลำดับก่อนหน้า
3) สมาชิกใน list เรียงลำดับแบบสุ่ม random order นั่นคือไม่มีลำดับ
4) สมาชิกใน list เป็นค่าเดียวกันหมด

หมายเหตุ

กำหนดให้มีฟังก์ชัน check_order(l) เพื่อตรวจสอบการเรียงลำดับสมาชิกใน list l และแสดงผลรูปแบบลำดับที่พบ
ให้แสดงข้อความโต้ตอบหรือข้อผิดพลาดที่อาจเกิดขึ้นในกรณีต่างๆ ดังนี้
“Number is out of range.”เมื่อคะแนนไม่อยู่ในช่วง 0 – 100 ซึ่งจะไม่ถูกนำมาคิดในลำดับสมาชิก
ถ้าลิสต์ว่าง ให้พิมพ์คำว่า "The list is empty."
ถ้าลิสต์เป็นกรณีที่ 1 ให้แสดงคำว่า "The list is in non-increasing order."
ถ้าลิสต์เป็นกรณีที่ 2 ให้แสดงคำว่า "The list is in non-decreasing order."
ถ้าลิสต์เป็นกรณีที่ 3 ให้แสดงคำว่า "The list is in random order."
ถ้าลิสต์เป็นกรณีที่ 4 ให้แสดงคำว่า "The list is in non-increasing and non-decreasing order."
คำเตือน

list.copy() มีใน python เวอร์ชัน 3.3 ขึ้นไปเท่านั้น ใน elab ไม่มีคำสั่งนี้ ให้นิสิตก็อปปี้ลิสต์เอง
ตัวอย่าง Input/Output 1
Enter a number (-1 to end): 1
Enter a number (-1 to end): 1
Enter a number (-1 to end): 2
Enter a number (-1 to end): 3
Enter a number (-1 to end): -1
-----
Original list:
[1, 1, 2, 3]
The list is in non-decreasing order.
ตัวอย่าง Input/Output 2
Enter a number (-1 to end): 3
Enter a number (-1 to end): 2
Enter a number (-1 to end): 1
Enter a number (-1 to end): -1
-----
Original list:
[3, 2, 1]
The list is in non-increasing order.'''

def check_order(l):
    if len(l) == 0:
        print("The list is empty.")
        return

    decreasing = True
    increasing = True

    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            increasing = False
        if l[i] < l[i - 1]:
            decreasing = False

    if decreasing and increasing:
        print("The list is in non-increasing and non-decreasing order.")
    elif decreasing:
        print("The list is in non-decreasing order.")
    elif increasing:
        print("The list is in non-increasing order.")

l = []
while True:
    n = int(input('Enter a number (-1 to end): '))
    if n == -1:
        break
    if n < 0 or n > 100:
        print('Number is out of range.')
        continue
    l.append(n)

print('-----')
print('Original list:')
print(l)
check_order(l)

