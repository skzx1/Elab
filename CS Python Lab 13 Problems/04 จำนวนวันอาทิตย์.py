'''จำนวนวันอาทิตย์
ให้เขียนโปรแกรมรับวันที่สองวัน โดยรูปแบบคือ วัน-เดือน ที่มีเครื่องหมาย "-" คั่นกลาง และวันกับเดือนเป็นเลขจำนวนเต็มสองหลักที่อาจมี 0 นำหน้า เช่นวันที่ 11 ธันวาคมจะเขียนเป็น "11-12" หรือวันที่ 3 สิงหาคมจะเขียนเป็น "03-08"

จากนั้นให้รับวันที่เป็นวันอาทิตย์แรกของเดือนมกราคม จากนั้นพิมพ์จำนวนวันอาทิตย์ที่อยู่ในช่วงของวันที่สองวันข้างต้น กำหนดให้เดือนกุมภาพันธ์มี 28 วัน

ข้อมูลที่ผิดพลาด

ถ้าเดือนที่รับเข้ามาผิดให้พิมพ์คำว่า "Wrong Month"
ถ้าวันที่ที่รับเข้ามาผิดหรือวันอาทิตย์แรกของเดือนมกราคมผิดให้พิมพ์คำว่า "Wrong Day"
ถ้าทั้งวันที่และเดือนผิดให้พิมพ์ "Wrong Month" ก่อน "Wrong Day" คนละบรรทัดกัน
พิมพ์ "Wrong Month" ครั้งเดียวแม้ว่าเดือนจะผิดทั้งสองวันที่ และพิมพ์ "Wrong Day" แค่ครั้งเดียวถึงแม้วันจะมากกว่าหนึ่งแห่งที่ผิด
ตัวอย่างข้อมูลเข้า/ข้อมูลออก

ข้อมูลเข้า	ข้อมูลออก
10-01
20-01
1	1
31-01
01-01
5	4
12-20
15-22
3	Wrong Month
50-10
15-22
10	Wrong Month
Wrong Day'''
day31 = [1, 3, 5, 7, 8, 10, 12]
day30 = [4, 6, 9, 11]
sundaycount = 0
dnm = input().split('-')
d1 = int(dnm[0])
m1 = int(dnm[1])
dnm2 = input().split('-')
d2 = int(dnm2[0])
m2 = int(dnm2[1])

wrong_month = False
wrong_day = False

if m1 > 12 or m2 > 12:
    wrong_month = True

if (m1 in day31 and d1 > 31) or (m2 in day31 and d2 > 31):
    wrong_day = True
elif (m1 in day30 and d1 > 30) or (m2 in day30 and d2 > 30):
    wrong_day = True
elif (m1 == 2 and d1 > 28) or (m2 == 2 and d2 > 28):
    wrong_day = True

if wrong_month:
    print('Wrong Month')
if wrong_day:
    print('Wrong Day')

sunday = int(input())
if sunday < 1 or sunday > 31 or (sunday % 7 != 0 and sunday % 7 != 1):
    print('Wrong Day')

start = 0
for i in range(1, m1):
    if i in day31:
       start += 31
    elif i in day30:
        start += 30
    elif i == 2:
        start += 28
start += d1
end = 0
for i in range(1, m2):
    if i in day31:
       end += 31
    elif i in day30:
        end += 30
    elif i == 2:
        end += 28
end += d2
while start <= end:
    if start % 7 == 0:
        sundaycount += 1
    start += 1
print(sundaycount)





