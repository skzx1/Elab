'''Guessing 1
จงเขียนโปรแกรมสำหรับเล่นเกมทายตัวเลข โดยกำหนดให้โปรแกรมสร้างเลขเป้าหมาย (target) ที่มีค่าตั้งแต่ 0 - 100 แล้วรับตัวเลขจากผู้เล่นที่ทายเข้ามา กำหนดให้เป้าหมายเท่ากับ 72

โปรแกรมที่เขียนต้องเทียบค่ากับตัวแปร target และไม่เปลี่ยนค่าของตัวแปร target

ตัวอย่าง Input/Output 1
Enter your guess (0 - 100): 111
Sorry, out of range, try again later.
ตัวอย่าง Input/Output 2
Enter your guess (0 - 100): 16
Sorry, your guess is wrong, try again later.
ตัวอย่าง Input/Output 3
Enter your guess (0 - 100): 72
Congratulations, your guess is correct.

'''
target = 72
x = int(input("Enter your guess (0 - 100): "))
if x < 0 or x > 100:
    print("Sorry, out of range, try again later.")
elif x < target or x > target:
    print("Sorry, your guess is wrong, try again later.")
else:
    print("Congratulations, your guess is correct.")