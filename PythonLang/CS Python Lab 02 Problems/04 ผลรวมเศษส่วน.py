'''ผลรวมเศษส่วน
จงเขียนโปรแกรมเพื่อรับค่าเศษ (numerator) และค่าส่วน (denominator) ของเศษส่วน (fraction) สองจำนวน แล้วคำนวณหาผลรวมของเศษส่วนทั้งสองจำนวน

สมมติให้เศษส่วนแรกอยู่ในรูป a/b และเศษส่วนที่สองอยู่ในรูป c/d ในที่นี้ให้แสดงผลลัพธ์ p/q ซึ่งเป็นผลรวมที่ได้ในรูปเศษส่วนเช่นกัน และไม่ต้องทำให้เป็นเศษส่วนอย่างต่ำ

ตัวอย่าง Input/Output (อักษรที่เส้นใต้เป็นสีแดงคือ input)##
First fraction:
>>Enter a numerator a: 3
>>Enter a denominator b: 8
Second fraction:
>>Enter a numerator c: 9
>>Enter a denominator d: 12
Summation of the two fractions is 108 / 96'''
print("First fraction:")
a = int(input(">>Enter a numerator a: "))
b = int(input(">>Enter a denominator b: "))

print("Second fraction:")
c = int(input(">>Enter a numerator c: "))
d = int(input(">>Enter a denominator d: "))

p = a * d + b * c
q = b * d

print(f"Summation of the two fractions is {p} / {q}")