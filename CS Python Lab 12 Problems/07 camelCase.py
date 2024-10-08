'''camelCase
camelCase คือวิธีการตั้งชื่อที่แต่ละคำจะอยู่ติดกันโดยไม่มีสัญลักษณ์คั่นกลาง โดยที่่คำแรกจะเป็นตัวอักษรตัวเล็กทั้งหมด ส่วนคำต่อๆ ไปจะขึ้นต้นคำด้วยตัวอักษรตัวใหญ่แต่ตัวอักษรอื่นจะเป็นตัวเล็ก เช่นคำว่า helloWorld หรือ goodGame แบบนี้ถือว่ามีรูปแบบเป็น camelCase

ให้เขียนโปรแกรมรับชื่อเข้ามาแล้วเปลี่ยนให้เป็น camelCase โดยชื่อที่รับเข้ามานั้นจะแบ่งคำด้วยสัญลักษณ์ - _ = . $ เท่านั้น
ไม่ทช่ .title() หรือ .capitalize() ในการแปลงชื่อ
ตัวอย่างข้อมูลเข้า/ข้อมูลออก

ข้อมูลเข้า	ข้อมูลออก
hello_world	helloWorld
A-very.long$name	aVeryLongName
hello     world helloWorld
_K.test    kTest
$ hello     world helloWorld'''
filename = input()
no = '-_=.$ '
idex = 0
firstname = filename[idex].lower()
if firstname in no:
    fliename = filename.replace('', '')
    filename = filename.replace(firstname, '')
    firstname = filename[idex].lower()
else:
    for i in filename:
        if i in no:
            filename = filename.replace(i, '')
            filename = filename[:idex] + filename[idex].upper() + filename[idex + 1:]
        else:
            idex += 1
fullname = firstname + filename[1:]
print(fullname)
