'''Histogram
จงเขียนโปรแกรมเพื่อรับคะแนนสอบย่อย (คะแนนเต็ม 10 ไม่มีคะแนนติดลบ) ของนักเรียนจำนวน 20 คน มาสร้างเป็น list แล้วแสดงผลคะแนนของนักเรียนทั้ง 20 คนในรูปแผนภาพฮิสโตแกรม เมื่อกำหนดให้สัญลักษณ์ดอกจัน 1 อัน หมายถึงนักเรียน 1 คนที่ได้คะแนนนั้นๆ

หมายเหตุ ให้แสดงข้อความแจ้งข้อความโต้ตอบหรือข้อผิดพลาดที่อาจเกิดขึ้นในกรณีต่างๆ ดังนี้

“Score is out of range.” เมื่อคะแนนไม่อยู่ในช่วง 0 – 10
ตัวอย่าง Input/Output 1
Enter score: 1
Enter score: 2
Enter score: 3
Enter score: 4
Enter score: 5
Enter score: 6
Enter score: 7
Enter score: 9
Enter score: 10
Enter score: 4
Enter score: 4
Enter score: 5
Enter score: 5
Enter score: 6
Enter score: 6
Enter score: 5
Enter score: 6
Enter score: 2
Enter score: 3
Enter score: 0
Original list:
[1, 2, 3, 4, 5, 6, 7, 9, 10, 4, 4, 5, 5, 6, 6, 5, 6, 2, 3, 0]
 0 *
 1 *
 2 **
 3 **
 4 ***
 5 ****
 6 ****
 7 *
 8 
 9 *
10 *'''

data = []
i = 0
while i < 20:
    x = int(input("Enter score: "))
    if x > 10 or x < 0:
        print("Score is out of range.")
    else:
        data.append(x)
        i += 1
print("Original list:")
print(data)
for i in range(11): 
    count = data.count(i)
    print(f"{i:2} " + "*" * count)