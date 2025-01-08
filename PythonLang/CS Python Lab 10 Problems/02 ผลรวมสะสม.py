'''ผลรวมสะสม
จงเขียนโปรแกรมเพื่อรับจำนวนเต็มใดๆ ที่มีค่าตั้งแต่ 1 ถึง 999 มาสร้างเป็น list (ใส่ 0 เพื่อหยุด) จากนั้นให้สร้างและแสดงผล list ใหม่ โดยที่สมาชิกลำดับที่ i ของ list ใหม่จะเป็นผลรวมสะสมของสมาชิก i+1 ตัวแรกของ list เดิม

หมายเหตุ

ให้แสดงข้อความโต้ตอบหรือข้อผิดพลาดที่อาจเกิดขึ้นในกรณีต่างๆดังนี้
“Number is out of range.” เมื่อคะแนนไม่อยู่ในช่วง 1 – 999
กำหนดให้มีฟังก์ชัน accum_sum(l) เพื่อสร้างและแสดงผลรวมสะสม list ใหม่จาก list l
ตัวอย่าง Input/Output 1
Enter a number (0 to end): 1
Enter a number (0 to end): 2
Enter a number (0 to end): 3
Enter a number (0 to end): 4
Enter a number (0 to end): 0
Original list:
[1, 2, 3, 4]
Accumulative Sum:
1
3
6
10
ตัวอย่าง Input/Output 2
Enter a number (0 to end): -1
Number is out of range.
Enter a number (0 to end): 5
Enter a number (0 to end): 10
Enter a number (0 to end): 2
Enter a number (0 to end): 3
Enter a number (0 to end): 4
Enter a number (0 to end): 0
Original list:
[5, 10, 2, 3, 4]
Accumulative Sum:
5
15
17
20
24'''
data = []
while True:
    x = int(input("Enter a number (0 to end): "))
    if x == 0:
        break
    elif x < 0 or x > 999:
        print("Number is out of range.")
    else:
      data.append(x)
print("Original list:")
print(data)
print("Accumulative Sum: ")

def accum_sum(l):
    sum = 0
    for i in range(len(l)):
        sum += l[i]
        print(sum)
accum_sum(data)
        

