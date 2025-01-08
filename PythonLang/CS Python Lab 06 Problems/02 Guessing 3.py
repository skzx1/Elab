'''Guessing 3 ทายตัวเลข (loop)
จงเขียนโปรแกรมสำหรับเล่นเกมทายตัวเลขที่มีค่าตั้งแต่ 0 – 100 โดยกำหนดให้โปรแกรมกำหนดค่าเป้าหมาย (target) สำหรับทาย จากนั้นให้รับจำนวนเต็ม 1 จำนวน แล้วเปรียบเทียบว่าจำนวนดังกล่าวมีค่ามากกว่า น้อยกว่า หรือเท่ากับค่าเป้าหมายที่กำหนดไว้หรือไม่

นอกจากนี้ให้ใช้โครงสร้างแบบทำซ้ำเพื่อให้มีการรับจำนวนเต็มเพื่อเปรียบเทียบกับค่าเป้าหมายในรอบถัดไปจนกว่าจะทายค่าเป้าหมายได้ถูกต้อง พร้อมกับให้นับจำนวนครั้งที่ใช้ทายจนได้ค่าเป้าหมาย (นับรวมครั้งที่ทายตัวเลขนอกช่วงที่กำหนดด้วย) แล้วแสดงผลจำนวนครั้งดังกล่าวก่อนสิ้นสุดการทำงาน

โดยกำหนด target = 72

หมายเหตุ ให้แสดงข้อความแจ้งข้อความโต้ตอบหรือข้อผิดพลาดที่อาจเกิดขึ้นในกรณีต่างๆ ดังนี้

“Sorry, your guess is out of range.” เมื่อตัวเลขที่ทายไม่อยู่ในช่วง 0 – 100
“Sorry, your guess is too low.” เมื่อตัวเลขที่ทายมีค่าน้อยกว่าค่าเป้าหมาย
“Sorry, your guess is too high.” เมื่อตัวเลขที่ทายมีค่ามากกว่าค่าเป้าหมาย
“Congratulations, your guess is correct. Total number of guesses is x.” เมื่อตัวเลขที่ทายมีค่าตรงกับค่าเป้าหมาย พร้อมจำนวนเต็ม x ซึ่งหมายถึงจำนวนครั้งในการทายทั้งหมด
ตัวอย่าง Input/Output 1
Enter your guess: 13
Sorry, your guess is too low.
Enter your guess: 1000
Sorry, your guess is out of range.
Enter your guess: 100
Sorry, your guess is too high.
Enter your guess: 35
Sorry, your guess is too low.
Enter your guess: 87
Sorry, your guess is too high.
Enter your guess: 38
Sorry, your guess is too low.
Enter your guess: 82
Sorry, your guess is too high.
Enter your guess: 44
Sorry, your guess is too low.
Enter your guess: 80
Sorry, your guess is too high.
Enter your guess: 50
Sorry, your guess is too low.
Enter your guess: 76
Sorry, your guess is too high.
Enter your guess: 72
Congratulations, your guess is correct.
Total number of guesses is 12.'''
c = 0
target = 72
while True:
    v = int(input("Enter your guess: "))
    if v > 100 or v < 0:
        print("Sorry, your guess is out of range.")
    elif v < target:
        print("Sorry, your guess is too low.")
    elif v > target:
        print("Sorry, your guess is too high.")
    else:
        print("Congratulations, your guess is correct.")
        print(f"Total number of guesses is {c+1}.")
        break
    c += 1