'''ค่าจอดรถ (ยากขึ้น)
จงเขียนโปรแกรมเพื่อรับจำนวนชั่วโมงและจำนวนนาที ที่ลูกค้านำรถเข้ามาจอดในลานจอดรถของห้างสรรพสินค้าแห่งหนึ่ง ซึ่งให้บริการระหว่างเวลา 06:00 – 02:00 น. (ระบบ 24 ชั่วโมง) เท่านั้น และมีอัตราค่าจอดรถเป็นดังนี้ 2 ชั่วโมงแรกจอดฟรี ชั่วโมงที่ 3 และ 4 ชั่วโมงละ 20 บาท ชั่วโมงที่ 5 เป็นต้นไปชั่วโมงละ 50 บาท และเศษของชั่วโมงปัดเป็น 1 ชั่วโมง นอกจากนี้เมื่อลูกค้าซื้อสินค้าตั้งแต่ 300 – 3,000 บาท ให้จอดฟรีเพิ่มในชั่วโมงที่ 3 และ 4 และเมื่อซื้อสินค้า 3,001 บาทขึ้นไป จอดฟรีตลอดเวลาที่ให้บริการ (ราคาสินค้าที่ซื้อไม่มีหน่วยสตางค์) แล้วให้แสดงผลค่าจอดรถที่ต้องชำระ

หมายเหตุ ให้แสดงข้อความแจ้งข้อผิดพลาด "Invalid time." ก่อนยุติการทำงาน ถ้าจำนวนชั่วโมงที่รับเข้ามามีค่าอยู่นอกช่วง 0 – 20 ชั่วโมงหรือเมื่อจำนวนนาทีที่รับเข้ามามีค่าอยู่นอกช่วง 0 – 59 นาที

คำแนะนำ นิสิตควรตรวจข้อมูลเข้าว่าเวลาจอดไม่เกินจำนวนชั่วโมงที่จอดรถได้

ตัวอย่าง Input/Output 1
Enter number of hours: 22
Enter number of minutes: 17
Enter shopping amount: 500
Invalid time.
ตัวอย่าง Input/Output 2
Enter number of hours: 7
Enter number of minutes: 32
Enter shopping amount: 1250
Total amount due is 200 Baht, thank you.
ตัวอย่าง Input/Output 3
Enter number of hours: 9
Enter number of minutes: 10
Enter shopping amount: 3050
No charge, thank you.
ตัวอย่าง Input/Output 4
Enter number of hours: 4
Enter number of minutes: 45
Enter shopping amount: 480
Total amount due is 50 Baht, thank you.
ตัวอย่าง Input/Output 5
Enter number of hours: 3
Enter number of minutes: 20
Enter shopping amount: 100
Total amount due is 40 Baht, thank you.
ตัวอย่าง Input/Output 6
Enter number of hours: 5
Enter number of minutes: 12
Enter shopping amount: 100
Total amount due is 140 Baht, thank you.'''
hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))
if hours < 0 or hours > 20 or minutes < 0 or minutes > 59  or (hours == 20 and minutes > 0):
    print("Invalid time.")
else:
    if minutes > 0:
        hours += 1
    if buyAmt >= 3001:
        print("No charge, thank you.")
    elif buyAmt >= 300:
        if hours <= 4:
            print("No charge, thank you.")
        else:
            charge = (hours - 4) * 50
            print(f"Total amount due is {charge} Baht, thank you.")
    else:
        if hours <= 2:
            print("No charge, thank you.")
        else:
            if hours <= 4:
                charge = (hours - 2) * 20
            else:
                charge = 2 * 20 + (hours - 4) * 50
            print(f"Total amount due is {charge} Baht, thank you.")