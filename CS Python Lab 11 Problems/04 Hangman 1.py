'''Hangman 1
Hangman เป็นเกมทายคำศัพท์ โดยผู้เล่นจะทราบเพียงแค่ จำนวน ตัวอักษรของศัพท์ที่ให้มาเท่านั้น ให้ผู้เล่นเลือกทายอักษรที่ผู้เล่นคาดว่า มีอยู่ในคำที่โจทย์ให้มา หากอักษรที่ผู้เล่นทาย ไม่มีในศัพท์ที่โจทย์ให้มา ผู้เล่นก็จะถูกแขวนคอ เริ่มจาก หัว ลำตัว แขนซ้าย แขนขวา ขาซ้าย ขาขวา เมื่อผิดครบทั้ง 6 ครั้ง จึงถือว่า เป็นการแขวนคออย่างเต็มตัว ผู้เล่นก็จะแพ้ในเกมนั้น หากผู้เล่นสามารถทายศัพท์ถูกก่อนขาขวาจะโดนแขวน ผู้เล่นก็จะชนะในเกมนั้น

โดยข้อนี้ จะตัดบางส่วนของโปรแกรมเต็ม นั่นคือส่วนนับจำนวนตัวอักษรที่ทายถูกแล้วจากจำนวนตัวอักษรทั้งหมด

ข้อมูลเข้า
บรรทัดแรก รับคำศัพท์ของโจทย์ที่ให้ผู้เล่นทาย โดยเป็นตัวอักษร a - z ตัวเล็กทั้งหมด ไม่มีช่องว่างหรืออักขระพิเศษอื่น และไม่เป็น string ว่าง มีจำนวนตัวอักษรทั้งหมดไม่เกิน 100 ตัวอักษร

บรรทัดถัดไป รับตัวอักษร (a-z ตัวเล็ก)ที่ผู้เล่นทายทีละตัว จนกว่าผู้เล่นจะใส่ 0

ข้อมูลออก
บรรทัดเดียว แสดงจำนวนตัวอักษรที่ผู้เล่นทายตรงกับโจทย์แล้ว และจำนวนตัวอักษรทั้งหมดในโจทย์ คั่นด้วยเครื่องหมาย /

ตัวอย่างข้อมูลเข้า/ข้อมูลออก
ข้อมูลเข้า	ข้อมูลออก
hangman
a
b
c
a
0	        2/7
thelonglengthword
a
e
o
u
i
0	        4/17'''
data = []
correct = 0
target = input()
while True:
    guess = input()
    if guess == '0':
        break
    else:
        for i in target :
            if guess == i and guess not in data:
                correct += 1
        data.append(guess)
print(f"{correct}/{len(target)}")