'''หารากที่สอง n ครั้ง
ให้นิสิตเขียนฟังก์ชันชื่อ sqrt_n_times(x, n) ที่จะคืนค่าที่เสมือนการนำค่า x มาหาค่ารากที่สองต่อเนื่องกันเป็นจำนวน n ครั้ง

ตัวอย่างผลลัพธ์เมื่อเรียกฟังก์ชัน

print( sqrt_n_times(10**8, 3) )

10.0'''

import math
def sqrt_n_times(x, n):
  while n > 0:
      x = math.sqrt(x)
      n -= 1
  return x
x = float(input())
n = int(input())
print( sqrt_n_times(x, n) )