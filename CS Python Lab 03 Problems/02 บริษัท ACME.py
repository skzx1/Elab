'''บริษัท ACME
บริษัท ACME จำกัด ต้องการให้ส่วนลดกับลูกค้าที่ซื้อสินค้าในมูลค่าตั้งแต่ 1,000 บาทขึ้นไป โดยถ้าลูกค้าซื้อสินค้าตั้งแต่ 1,000 ขึ้นไปแต่น้อยกว่า 3,000 บาท ให้ส่วนลด 10% และถ้าซื้อสินค้าตั้งแต่ 3,000 บาทขึ้นไป ให้ส่วนลด 15% จงเขียนโปรแกรมที่รับจำนวนราคาสินค้าแล้วคำนวนเงินสุทธิที่ลูกค้าต้องชำระ

ตัวอย่างข้อมูล
Enter buying amount: 4200.0
Amount due after discount is 3570.00 baht.'''
a = float(input('Enter buying amount: '))
if a >= 1000 and a < 3000 :
    ar = a - (a * (10 / 100)) 
    print(f'Amount due after discount is {ar:.2f} baht.')
elif a >= 3000 :
    ae = a - (a * (15 / 100)) 
    print(f'Amount due after discount is {ae:.2f} baht.')  
else :
    print(f'Amount due after discount is {a:.2f} baht.')