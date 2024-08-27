'''ฟังก์ชันทางคณิตศาสตร์
จงเปลี่ยนนิพจน์ทางคณิตศาสตร์ข้างล่างนี้เป็นนิพจน์ทางคณิตศาสตร์ในภาษา Python ที่ถูกต้อง

a
1
=
x
y
+
z
a
2
=
cos
(
2
π
)
+
log
e
(
x
)
a
3
=
|
x
|
+
|
y
|
a
4
=
√
x
2
+
y
2
+
z
2
a
5
=
sin
2
(
x
)
+
cos
2
(
x
)
a
6
=
5
√
x
+
y
a
7
=
e
x
ln
y
หมายเหตุ: สำหรับค่าพายให้ใช้ค่าคงที่ math.pi และค่า e ให้ใช้ค่าคงที่ math.e

ดูรายละเอียดของตัวแปรและฟังก์ชันในโมดูล math ได้ที่ https://docs.python.org/3.6/library/math.html

วัตถุประสงค์ของโจทย์ข้อนี้ ต้องการให้นิสิตอ่าน documentation

ตัวอย่าง Input/Output
Enter x: 5.0
Enter y: 5.0
Enter z: 5.0
a1 = 3130.00
a2 = 2.61
a3 = 10.00
a4 = 8.66
a5 = 1.00
a6 = 1.58
a7 = 3125.00'''
import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))
a1 = x ** y + z
a2 = math.cos(2 * math.pi) + math.log(x)
a3 = abs(x) + abs(y)
a4 = math.sqrt(x**2 + y**2 + z**2)
a5 = math.sin(x)**2 + math.cos(x)**2
a6 = (x + y) ** (1/5)
a7 = math.e ** (x * math.log(y))
print(f"a1 = {a1:.2f}")
print(f"a2 = {a2:.2f}")
print(f"a3 = {a3:.2f}")
print(f"a4 = {a4:.2f}")
print(f"a5 = {a5:.2f}")
print(f"a6 = {a6:.2f}")
print(f"a7 = {a7:.2f}")