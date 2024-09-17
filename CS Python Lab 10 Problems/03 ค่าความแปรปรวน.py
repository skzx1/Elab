'''ค่าความแปรปรวน
จงเขียนโปรแกรมเพื่อรับคะแนนสอบวิชาภาษาไทยของนักเรียน (คะแนนเต็ม 100 ไม่มีคะแนนติดลบ) จนกระทั่งผู้ใช้ป้อนข้อมูล -1 จึงหยุด จากนั้นสร้าง list ของข้อมูล แล้วแสดงผลคะแนนมากที่สุด (maximum score) คะแนนน้อยที่สุด (minimum score) คะแนนเฉลี่ย (average score) และส่วนเบี่ยงเบนมาตรฐาน(standard deviation)

S
.
D
.
=
√
∑
n
i
=
1
(
x
i
−
¯
x
)
2
n
−
1
หมายเหตุ

ให้แสดงข้อความโต้ตอบหรือข้อผิดพลาดที่อาจเกิดขึ้นในกรณีต่างๆ ดังนี้
“Score is out of range.” เมื่อคะแนนไม่อยู่ในช่วง 0 – 100

กำหนดให้มีฟังก์ชัน find_sd(l) เพื่อส่งกลับส่วนเบี่ยงเบนมาตรฐานของ list l
แสดงผลคะแนนมากที่สุด คะแนนน้อยที่สุด คะแนนเฉลี่ย และส่วนเบี่ยงเบนมาตรฐาน เมื่อมีข้อมูลใน list เท่านั้น
ตัวอย่าง Input/Output
Enter score: 34.0
Enter score: 101
Score is out of range.
Enter score: 80.5
Enter score: 22.75
Enter score: 56.0
Enter score: 78.25
Enter score: 92.25
Enter score: 69.0
Enter score: 78.5
Enter score: 83.0
Enter score: 46.75
Enter score: -1
Maximum score is 92.25.
Minimum score is 22.75.
Average score is 64.10.
Standard deviation is 23.17.'''
data = []
while True:
    x = float(input("Enter score: "))
    if x == -1:
        break
    elif x < 0 or x > 100:
        print("Score is out of range.")
    else:
      data.append(x)
