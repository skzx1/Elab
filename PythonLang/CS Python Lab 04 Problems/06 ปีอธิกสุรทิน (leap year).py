'''ปีอธิกสุรทิน (leap year)
จงเขียนโปรแกรมเพื่อรับค่าปีคริสตศักราชแล้วแสดงผลว่าปีดังกล่าวเป็นปีอธิกสุรทินหรือไม่ โดยปีอธิกสุรทินหมายถึง

ปีที่หารด้วย 4 ลงตัว ยกเว้นเฉพาะปีที่หารด้วย 100 ลงตัวด้วย
ปีที่หารด้วย 400 ลงตัว
ถ้าข้อมูลเข้าผิดพลาด ให้พิมพ์คำว่า "Invalid year."

ตัวอย่าง Input/Output 1
Enter year: 1900
1900 is not a leap year.
ตัวอย่าง Input/Output 2
Enter year: 1996
1996 is a leap year.
ตัวอย่าง Input/Output 3
Enter year: 2000
2000 is a leap year.
ตัวอย่าง Input/Output 4
Enter year: 2012
2012 is a leap year.
ตัวอย่าง Input/Output 5
Enter year: 2100
2100 is not a leap year.'''
x = int(input("Enter year: "))
if x <= 0:
    print("Invalid year.")
else:    
    if x % 4 == 0 and  x % 100 != 0 or x % 400 == 0:
        print (f"{x} is a leap year.")
    else:
        print(f"{x} is not a leap year.")