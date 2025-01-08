'''จะบวกแบบไหน
เขียนโปรแกรมเพื่อแสดงผลลัพธ์โดยใช้ operator +

ตัวแปรเริ่มต้น
a เป็นสตริงของจำนวนเต็ม
b เป็นสตริงของจำนวนเต็ม

ข้อมูลออก
บรรทัดแรก แสดงข้อความ "Addition: " ตามด้วย ผลบวกของจำนวนเต็ม a และ b
บรรทัดที่สอง แสดงข้อความ "Concatenation: " ตามด้วย ข้อความที่เป็นการเชื่อม (concatenate) ระหว่าง a และ b
ตัวอย่าง Output เมื่อ a มีค่า "345" และ b มีค่า "440"
Addition: 785
Concatenation: 345440
ตัวอย่าง Output เมื่อ a มีค่า "0" และ b มีค่า "0"
Addition: 0
Concatenation: 00'''
a = "354"
b = "440"
add = int(a) + int(b)
con = a+b
print ("Addition:" ,add)
print ("Concatenation:",con)