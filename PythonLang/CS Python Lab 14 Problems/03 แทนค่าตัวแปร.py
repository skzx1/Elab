'''แทนค่าตัวแปร
จงเขียนโค้ดเพื่อช่วยแทนค่าตัวแปรในโปรแกรมจำลอง

โดยเริ่มต้นต้องกำหนดค่าให้กับตัวแปรก่อน หลังจากนั้น จึงสร้างโปรแกรมจำลองที่ใช้ตัวแปรเหล่านั้น

โดยตัวแปรที่ใช้ในโปรแกรมจะมีเครื่องหมายปีกกา ({}) ครอบดังตัวอย่างด้านล่าง

โค้ดของนิสิตจะต้องแทนค่าตัวแปรในโปรแกรมจำลอง และพิมพ์ผลลัพธ์หลังการแทนค่าออกมา

ให้ใช้ -1 เป็นการระบุว่า ได้กำหนดค่าตัวแปรเสร็จสิ้นและสร้างโปรแกรมจำลองเสร็จสิ้น

ตัวอย่างผลลัพธ์ที่ 1
Enter variables and values:
x = 5
y = 6
-1
Enter your program:
z = {x} + {y}
print({x})
print({y})
-1
Result:
z = 5 + 6
print(5)
print(6)'''
variables = {}
print('Enter variables and values:')
while True:
   word = input()
   if word == '-1':
      break
   [var, val] = word.split('=')
   var = var.strip()
   val = val.strip()
   variables[var] = val

lines = []
print('Enter your program:')
while True:
   word = input()
   if word == '-1':
      break
   for var in variables:
      key = '{' + var + '}'
      word = word.replace(key, variables[var])
   lines.append(word)
print('Result:')
for line in lines:
    print(line)