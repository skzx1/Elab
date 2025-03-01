'''Cloth Size
สมมติว่าเจ้าของบริษัทต้องการตัดเสื้อให้พนักงานทุกคน จึงต้องการทราบว่า ควรซื้อเสื้อแต่ละขนาดเป็นจำนวนกี่ตัว

จงเขียนฟังก์ชัน cloth_size(width_list) เพื่อช่วยเจ้าของบริษัทคำนวณ

โดยฟังก์ชันนี้รับลิสต์ width_list ที่เก็บรายการขนาดรอบอกของพนักงานทุกคน

และคืนค่าเป็น dictionary ที่เก็บจํานวนเสื้อแต่ละขนาด

โดยรอบอกที่เล็กกว่าหรือเท่ากับ 36 จะเป็นขนาด S

รอบอกที่ใหญ่กว่า 36 แต่ไม่เกิน 44 จะเป็นขนาด M

และรอบอกที่มากกว่า 44 จะเป็นขนาด L

หมายเหตุ ห้ามใช้คำสั่ง count

ตัวอย่างการทำงาน
 
>>> print(cloth_size([50, 44, 40, 48]))
{'S': 0, 'M': 2, 'L': 2}'''
def cloth_size(width_list):
    asw = {'S': 0, 'M': 0, 'L': 0}
    for width in width_list:
        if width <= 36:
            asw['S'] += 1
        elif width > 44:
            asw['L'] += 1
        else:
            asw['M'] += 1
    return asw