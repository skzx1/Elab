'''Electric Appliance Store
ร้านขายเครื่องใช้ไฟฟ้าแห่งหนึ่ง นำเครื่องใช้ไฟฟ้าสามชนิดมาลดราคา ได้แก่ โทรทัศน์ (TV) เครื่องเล่นดีวีดี (DVD player) และเครื่องเสียง (Audio System) โดยสินค้าแต่ละชนิดจะมีราคาแตกต่างกันดังตารางนี้

Product	Price per unit (bahts)
TV	6000
DVD player	1500
Audio System	3000
ร้านค้ามอบส่วนลดพิเศษ 20% ให้กับลูกค้าที่มียอดซื้อ (price) อย่างน้อย 24,000 บาท

เขียนโปรแกรมเพื่อรับจำนวนสินค้าแต่ละชนิดที่ลูกค้าจะซื้อ (เป็นจำนวนเต็มบวกหรือศูนย์) แล้วคำนวณยอดซื้อ และแสดง 1. ยอดซื้อรวม (total price) 2. ส่วนลด (discount) ถ้ามี และ 3. ราคาที่ต้องชำระ (payment) ดังตัวอย่าง โดยราคาให้แสดงด้วยทศนิยม 2 ตำแหน่ง

Example 1
How many TVs? 1
How many DVD players? 0
How many Audio Systems? 1
Total price is 9000.00 baht.
Your payment is 9000.00 baht. Thank you!
Example 2
How many TVs? 0
How many DVD players? 2
How many Audio Systems? 3
Total price is 12000.00 baht.
Your payment is 12000.00 baht. Thank you!
Example 3
How many TVs? 5
How many DVD players? 4
How many Audio Systems? 3
Total price is 45000.00 baht.
You've got a discount of 9000.00 baht.
Your payment is 36000.00 baht. Thank you!

'''
x = int(input("How many TVs? "))
y = int(input("How many DVD players? "))
z = int(input("How many Audio Systems? "))
xl = x * 6000
yl = y * 1500
zl = z * 3000
tl = xl + yl + zl
if tl >= 24000:
    di = (tl*(20/100))
    tp = tl - di
    print(f"Total price is {tl:.2f} baht.")
    print(f"You've got a discount of {di:.2f} baht.")
    print(f"Your payment is {tp:.2f} baht. Thank you!")
else :
    print(f"Total price is {tl:.2f} baht.")
    print(f"Your payment is {tl:.2f} baht. Thank you!")