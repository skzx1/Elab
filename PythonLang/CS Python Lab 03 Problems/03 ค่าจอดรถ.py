'''ค่าจอดรถ
จงเขียนโปรแกรมเพื่อรับจำนวนชั่วโมง และจำนวนนาทีที่ลูกค้านำรถเข้ามาจอดในลานจอดรถแห่งหนึ่ง ซึ่งมีอัตราค่าจอดรถเป็นดังนี้ 15 นาทีแรกฟรี, 2 ชั่วโมงแรก 10 บาท และชั่วโมงที่สามเป็นต้นไปคิดเพิ่มชั่วโมงละ 10 บาท และเศษของชั่วโมงปัดเป็น 1 ชั่วโมง แล้วให้แสดงผลค่าจอดรถที่ต้องชำระ

หมายเหตุ: ต้องตรวจสอบข้อมูลเข้าด้วยว่าถูกต้องหรือไม่ หากไม่ถูกต้องให้แสดงข้อความว่า "Input Error!"

ตัวอย่าง Input/Output 1
Enter number of hours: 4
Enter number of minutes: 17
Total amount due is 40 Bahts.
ตัวอย่าง Input/Output 2
Enter number of hours: 0
Enter number of minutes: 12
No charge, thanks.'''
import math
h = int(input("Enter number of hours: "))
m = int(input("Enter number of minutes: "))

if h < 0 or m < 0 or m >= 60:
    print("Input Error!")
else:
    if h == 0 and m <= 15:
        print("No charge, thanks.")
    else:
        if m > 0:
            thours = h + 1
        else:
            thours = h
        if thours <= 2:
            tcost = 10
        else:
            tcost = 10 + (thours - 2) * 10
        
        print(f"Total amount due is {tcost} Bahts.")