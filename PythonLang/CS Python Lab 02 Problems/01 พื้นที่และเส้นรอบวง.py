'''พื้นที่และเส้นรอบวง
จงเขียนโปรแกรมเพื่อคำนวณหาพื้นที่วงกลมและเส้นรอบวงของวงกลมที่มีรัศมี r

กำหนดให้ข้อมูลเข้าเป็นเลขจำนวนเต็มเท่านั้น แสดงพื้นที่และเส้นรอบวงเป็นเลขจำนวนจริงทศนิยม 2 ตำแหน่ง

แนะนำ ใช้ตัวแปร math.pi ใน module math แทนค่า Pi

ข้อมูลเข้า
บรรทัดเดียว แสดงข้อความ "Enter a radius: " และรอรับจำนวนเต็ม r ซึ่งไม่เป็นลบ แทนรัศมีของวงกลม

ข้อมูลออก
บรรทัดแรก แสดงข้อความ "Area of a circle with radius " ตามด้วยค่า r ตามด้วย " is " ตามด้วยพื้นที่ของวงกลมรัศมี r
บรรทัดที่สอง แสดงข้อความ "Circumference of a circle with radius " ตามด้วยค่า r ตามด้วย " is " ตามด้วยเส้นรอบวงของวงกลมรัศมี r
ตัวอย่าง Input/Output
Enter a radius: 3
Area of a circle with radius 3 is 28.27
Circumference of a circle with radius 3 is 18.85'''
import math
r = int(input("Enter a radius: "))
a = math.pi * r ** 2
b = math.pi * r * 2
print(f"Area of a circle with radius {r} is {a:.2f}")
print(f"Circumference of a circle with radius {r} is {b:.2f}")