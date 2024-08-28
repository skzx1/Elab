'''Master Mind
เกม Master Mind เป็นเกมทายตัวเลขของผู้เล่น 2 คน ผู้เล่นคนแรกตั้งจำนวนเต็มขึ้นมา 1 จำนวน ซึ่งกำหนดให้แต่ละหลักมีค่าไม่ซ้ำกัน แล้วให้ผู้เล่นอีกคนหนึ่งทาย

ให้เขียนโปรแกรมเพื่อรับจำนวนเต็ม 2 จำนวน ที่มีขนาด 4 หลัก จำนวนแรกเป็นของผู้เล่น 1 และจำนวนที่สองเป็นของผู้เล่น 2
ให้โปรแกรมแสดงผลว่าผู้เล่น 2 ทายตัวเลขได้ถูกต้องกี่ตัว (digits) และกี่ตำแหน่ง (positions)

ในกรณีที่ทายถูกทุกตัวและทุกตำแหน่ง ให้แสดงข้อความ “Congratulations, you just mastered my mind!!”

ทั้งนี้ กำหนดให้ในการเปรียบเทียบความถูกต้องของตัวเลขและตำแหน่งของตัวเลข ต้องเป็นการดำเนินการของจำนวนเต็มเท่านั้น (ไม่อนุญาตให้ใช้การทำงานในแบบ string หรือ list)

หมายเหตุ
ตามหลักไวยากรณ์ภาษาอังกฤษ no จะตามด้วย noun เอกพจน์ หรือพหูพจน์ก็ได้ ในข้อนี้ให้ตามด้วย noun พหูพจน์

ตัวอย่าง 1

Enter a target (4-digit integer): 1234
Enter your guess (4-digit integer): 5341
No positions correct, three digits correct
ตัวอย่าง 2

Enter a target (4-digit integer): 1234
Enter your guess (4-digit integer): 1234
Congratulations, you just mastered my mind!!
ตัวอย่าง 3

Enter a target (4-digit integer): 1234
Enter your guess (4-digit integer): 1358
One position correct, one digit correct
สังเกตว่า เลข 1 เป็นเลขที่มีตำแหน่งตรงกัน (จึงนับว่าทายตำแหน่งถูก แต่ไม่นับเป็นเลขที่ทายถูก) และ เลข 3 เป็นเลขที่ทายถูก แต่มีตำแหน่งไม่ตรงกัน (จึงนับว่าเป็นเลขที่ทายถูก แต่ทายตำแหน่งไม่ถูก)
ตัวอย่าง 4

Enter a target (4-digit integer): 1234
Enter your guess (4-digit integer): 5678
No positions correct, no digits correct'''
target = int(input("Enter a target (4-digit integer): "))
guess = int(input("Enter your guess (4-digit integer): "))
position = 0
c = 0
gtarget = target
gguess = guess
t4 = target % 10
target //= 10
t3 = target % 10
target //= 10
t2 = target % 10
target //= 10
t1 = target % 10

g4 = guess % 10
guess //= 10
g3 = guess % 10
guess //= 10
g2 = guess % 10
guess //= 10
g1 = guess % 10

if t1 == g1:
    position += 1
elif t1 == g2 or t1 == g3 or t1 == g4:
    c += 1

if t2 == g2:
    position += 1
elif t2 == g1 or t2 == g3 or t2 == g4:
    c += 1

if t3 == g3:
    position += 1
elif t3 == g1 or t3 == g2 or t3 == g4:
    c += 1

if t4 == g4:
    position += 1
elif t4 == g1 or t4 == g2 or t4 == g3:
    c += 1

if position == 0:
    position = "No"
elif position == 1:
    position = "One"
elif position == 2:
    position = "Two"
elif position == 3:
    position = "Three"
elif position == 4:
    position = "four"
    
if c == 0:
    c = "no"
elif c == 1:
    c = "one"
elif c == 2:
    c = "two"
elif c == 3:
    c = "three"
elif c == 4:
    c = "four"
if gtarget == gguess:
    print("Congratulations, you just mastered my mind!!")
else:
    if (position == "No" and c == "No"):
       print("No positions correct, no digits correct")
    elif (position == "One" and c == 'one'):
       print(f"{position} position correct, {c} digit correct")
    elif (position == 'One'):
       print(f"{position} position correct, {c} digits correct")
    elif (c == 'one'):
       print(f"{position} positions correct, {c} digit correct")
    elif (position == "No" and c != "one"):
       print(f'No positions correct, {c} digits correct')
    elif (c == "no" and position != "One"):
       print(f"{position} positions correct, no digits correct")
    else:
       print(f"{position} positions correct, {c} digits correct")
