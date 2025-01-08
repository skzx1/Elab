'''ฐานนิยม
จงเขียนโปรแกรมเพื่อรับคะแนนสอบย่อย (คะแนนเต็ม 10 ไม่มีคะแนนติดลบ) ของนักเรียนจานวน 20 คน มาสรา้งเป็น list แล้วแสดงผลฐานนิยม (mode–จำนวนในรายการที่มีความถี่สูงที่สุด) ของ list ดังกล่าว

หมายเหตุ ให้แสดงข้อความแจ้งข้อความโต้ตอบหรือข้อผิดพลาดที่อาจเกิดขึ้นในกรณีต่างๆ ดังนี้

“Score is out of range.” เมื่อคะแนนไม่อยู่ในช่วง 0 – 10
กำหนดให้มีฟังก์ชัน find_mode(l) เพื่อแสดงผลฐานนิยมของ list l
ในกรณีที่มีจำนวนที่มีความถี่สูงสุดเท่ากันมากกว่า 1 จำนวน จำนวนเหล่านั้นทุกจำนวนเป็นฐานนิยม โดยให้แสดงผลลัพธ์จากน้อยไปหามาก บรรทัดละ 1 จำนวน
ตัวอย่าง Input/Output 1
Enter score: 10
Enter score: 8
Enter score: 4
Enter score: 4
Enter score: 11
Score is out of range.
Enter score: 4
Enter score: 0
Enter score: -1
Score is out of range.
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
Enter score: 4
-----
Original list:
[10, 8, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
Mode of scores:
4
ตัวอย่าง Input/Output 1
Enter score: 6
Enter score: 6
Enter score: 6
Enter score: 6
Enter score: 6
Enter score: 6
Enter score: 6
Enter score: 6
Enter score: 6
Enter score: 6
Enter score: 7
Enter score: 7
Enter score: 7
Enter score: 7
Enter score: 7
Enter score: 7
Enter score: 7
Enter score: 7
Enter score: 7
Enter score: 7
-----
Original list:
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
Mode of scores:
6
7'''
data = []
while len(data) < 20:
    x = int(input("Enter score: "))
    if x < 0 or x > 10:
        print("Score is out of range.")
    else:
        data.append(x) 
def find_mode(l):
    counts = [0] * 11 
    for num in l:
        counts[num] += 1
    max_c = max(counts)

    mode = []
    for score in range(11):
        if counts[score] == max_c:
            mode.append(score)
    for num in mode:
        print(num)
print("-----")
print("Original list: ")
print(data)
print("Mode of scores:")
find_mode(data)

