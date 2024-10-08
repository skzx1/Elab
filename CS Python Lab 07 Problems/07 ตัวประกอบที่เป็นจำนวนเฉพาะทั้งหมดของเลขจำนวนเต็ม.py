'''ตัวประกอบที่เป็นจำนวนเฉพาะทั้งหมดของเลขจำนวนเต็ม
จงเขียนโปรแกรมเพื่อรับเลขจำนวนเต็มบวกจากผู้ใช้ และหาตัวประกอบที่เป็นจำนวนเฉพาะทั้งหมดของค่านั้น โดยจะพิมพ์ตัวประกอบทีละตัวโดยเรียงจากตัวประกอบที่มีค่าน้อยที่สุดก่อนและพิมพ์ตัวประกอบหนึ่งตัวต่อหนึ่งบรรทัด ผลคูณของตัวประกอบทั้งหมดต้องเป็นจำนวนเต็มนั้น

หมายเหตุ: 1 ไม่นับเป็นจำนวนเฉพาะและไม่มีตัวประกอบด้วย ถ้าข้อมูลเข้าเป็น 1 นั้นไม่ต้องพิมพ์อะไรเลย

คำแนะนำ: ไม่ต้องกังวลเรื่องการหาจำนวนเฉพาะ ให้เริ่มจากจำนวนเฉพาะค่าแรกคือ 2 เมื่อแยกตัวประกอบของ 2 (ถ้าแยกได้) ออกมาจากเลขนั้นหมดแล้ว จำนวนอื่นที่มี 2 เป็นตัวประกอบจะไม่สามารถหารค่าที่เหลือลงตัวได้อีกต่อไป เช่นเมื่อเราแยก 300 = 2 x 2 x 75 แล้ว จำนวนอื่นที่มี 2 เป็นตัวประกอบเช่น 4, 6, หรือ 8 จะไม่มีทางหาร 75 ลงตัวได้

ข้อความโต้ตอบ

ให้พิมพ์คำว่า “Enter positive integer: “ เพื่อรับข้อมูลจากผู้ใช้
ให้พิมพ์คำว่า “Invalid number.” ถ้าขอบเขตของข้อมูลเข้าไม่เป็นไปตามที่กำหนด
ตัวอย่าง Input/Output 1
Enter positive integer: 300
2
2
3
5
5
ตัวอย่าง Input/Output 2
Enter positive integer: 1
ตัวอย่าง Input/Output 3
Enter positive integer: 13
13
ตัวอย่าง Input/Output 4
Enter positive integer: 0
Invalid number.'''
x = int(input("Enter positive integer: "))
if x <= 0:
 print("Invalid number.") 
 
else:
    i = 2
    while x > 1:
      if x % i == 0:
          print(i)
          x //= i
      else: 
          i += 1
       