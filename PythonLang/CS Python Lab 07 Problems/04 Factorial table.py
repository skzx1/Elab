'''Factorial table
จงเขียนโปรแกรมรับจำนวนเต็มใดๆ ที่มีค่ามากกว่าหรือเท่ากับศูนย์มาหนึ่งจำนวน จากนั้นคำนวณและแสดงผลลัพธ์ดังตัวอย่าง

หมายเหตุ ให้แสดงข้อความโต้ตอบหรือข้อผิดพลาดที่อาจเกิดขึ้นในกรณีต่างๆ ดังนี้

“Invalid input, program terminates.” เมื่อจำนวนเต็มที่รับเข้ามามีค่าน้อยกว่า 0
ไม่อนุญาตให้ใช้ sys.exit()
ไม่อนุญาตให้ใช้โมดูล math
ตัวอย่าง Input/Output
Enter a number: 5
0! = 1 = 1
1! = 1 = 1
2! = 2 x 1 = 2
3! = 3 x 2 x 1 = 6
4! = 4 x 3 x 2 x 1 = 24
5! = 5 x 4 x 3 x 2 x 1 = 120'''
num = int(input("Enter a number: "))
if num < 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    while i <= num:
        j = i
        fac = 1
        
        if i == 0:
            facex = "0! = 1 = 1"
        else:
            facex = f"{i}! = "
        
            while j > 0:
                fac *= j
                facex += f"{j}"
                if j > 1:
                    facex += " x "
                j -= 1
            
            facex += f" = {fac}"
        print(facex)
        i += 1
