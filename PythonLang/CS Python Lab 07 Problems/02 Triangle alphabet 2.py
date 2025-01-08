'''Triangle alphabet 2
จงเขียนโปรแกรมเพื่อรับจำนวนเต็มใดๆ ที่มีค่ามากกว่าศูนย์แต่ไม่เกิน 26 มาหนึ่งจำนวน แล้วแสดงรูปผลลัพธ์ที่สอดคล้องกับค่าที่รับเข้ามา

ฟังก์ชัน ord('A') เปลี่ยน character 'A' เป็น รหัส ascii ของ A ซึ่งเป็นจำนวนเต็ม
ฟังก์ชัน chr(65) เปลี่ยน รหัส ascii 65 เป็น character ของรหัส ascii 65
chr(ord('A')) ได้ character 'A'
chr(ord('A') + 1) ได้ character 'B'
ข้อความโต้ตอบ

“Invalid input, program terminates.” เมื่อจำนวนเต็มที่รับเข้ามามีค่าน้อยกว่าหรือเท่ากับ 0 หรือมากกว่า 26
ตัวอย่าง Input/Output
Enter a number: 5
ABCDE
ABCD
ABC
AB
A'''
def display(row):
   re = ''
   r = 0
   while r < row:
      ch = ord('A') + r
      re += chr(ch)
      r+=1
   print(re)
   
x = int(input("Enter a number: "))
if x <= 0 or x > 26 :
   print("Invalid input, program terminates.")
else:
   i = x
   while i >= 1:
      display(i)
      
      i -= 1
  