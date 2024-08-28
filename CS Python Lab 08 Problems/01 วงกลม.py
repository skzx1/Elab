'''วงกลม
จงเขียนโปรแกรมเพื่อรับรัศมี (radius) r ในโปรแกรมหลัก สร้างและเรียกใช้ฟังก์ชันต่อไปนี้ เพื่อให้แสดงผลลัพธ์
1.1. circle(r) เพื่อคำนวณและส่งกลับพื้นที่ของวงกลมที่มีรัศมี r
1.2. circumference(r) เพื่อคำนวณและส่งกลับความยาวเส้นรอบวงของวงกลมที่มีรัศมี r
1.3. sphere(r) เพื่อคำนวณและส่งกลับปริมาตรทรงกลมที่มีรัศมี r

ตัวอย่าง Input/Output
Enter a radius: 3.5
Area of a circle with radius 3.50 is 38.48.
Circumference of a circle with radius 3.50 is 21.99.
Volume of sphere with radius 3.50 is 179.59.'''
import math
def circle(r):
    a = math.pi * r**2
    return a
def circumference(r):
    a = 2 * math.pi * r
    return a
def sphere(r):
    a = 4/3 * math.pi * r**3
    return a

r = float(input("Enter a radius: "))
print('Area of a circle with radius {:.2f} is {:.2f}.'.format(r, circle(r)))
print('Circumference of a circle with radius {:.2f} is {:.2f}.'.format(r, circumference(r)))
print('Volume of sphere with radius {:.2f} is {:.2f}.'.format(r, sphere(r)))