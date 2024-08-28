'''Double rectangle stars
จงเขียนโปรแกรมเพื่อรับจำนวนเต็มใดๆ ที่มีค่ามากกว่าศูนย์มาสองจำนวน ที่เป็นความกว้างและความยาว แล้วแสดงรูปผลลัพธ์ที่สอดคล้องกับค่าที่รับเข้ามา

ทั้งนี้ กำหนดให้ใช้คำสั่ง

print(' *',end=''),

print('* ',end='') และ

print()

ได้เพียงอย่างละ 1 คำสั่งเท่านั้น

หมายเหตุ ให้แสดงข้อความเมื่อมีข้อผิดพลาดในกรณีดังนี้

“Invalid input, program terminates.” เมื่อความกว้างหรือความยาวที่รับเข้ามามีค่าน้อยกว่าหรือเท่ากับ 0
ตัวอย่าง Input/Output
Enter height: 5
Enter width: 6
* * * * * *
 * * * * * *
* * * * * *
 * * * * * *
* * * * * *'''
height = int(input("Enter height: "))
width = int(input("Enter width: "))

if height <= 0 or width <= 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    while height > i:
        if i % 2 == 0:
            print('* ' * width)
        else:
            print(' *' * width)
        i += 1