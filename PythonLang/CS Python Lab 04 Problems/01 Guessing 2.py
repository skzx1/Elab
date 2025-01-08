'''Guessing 2
จงเขียนโปรแกรมสำหรับเล่นเกมทายตัวเลข โดยกำหนดให้โปรแกรมสร้างเลขเป้าหมาย (target) คือค่า 72 แล้วรับตัวเลขจากผู้เล่นที่ทายเข้ามา
โดยให้เพิ่มการเปรียบเทียบเพื่อบอกผลการทายตัวเลขในกรณีที่ทายไม่ถูกเป็น 3 กรณี คือ มากกว่าค่าเป้าหมาย (too high), น้อยกว่าค่าเป้าหมาย (too low) และเท่ากับค่าเป้าหมาย

โปรแกรมที่เขียนต้องเทียบค่ากับตัวแปร target และไม่เปลี่ยนค่าของตัวแปร target

ตัวอย่าง Input/Output 1
Enter your guess (0 - 100): 45
Sorry, your guess is too low, try again later.
ตัวอย่าง Input/Output 2
Enter your guess (0 - 100): 99
Sorry, your guess is too high, try again later.
ตัวอย่าง Input/Output 3
Enter your guess (0 - 100): 72
Congratulations, your guess is correct.
ตัวอย่าง Input/Output 4
Enter your guess (0 - 100): -5
Sorry, out of range, try again later.'''
target = 72
x = int(input("Enter your guess (0 - 100): "))
if x < 0 or x > 100:
    print("Sorry, out of range, try again later.")
elif x < target :
    print("Sorry, your guess is too low, try again later.")
elif x > target :
    print("Sorry, your guess is too high, try again later.")    
else:
    print("Congratulations, your guess is correct.")