'''ถอดรหัสเด็กงี่เง่า
ลูคัสเริ่มงี่เง่ากับคาบแลปคอมอีกแล้ว แทนที่เขาจะเขียนโปรแกรม เขากลับมานั่งเข้ารหัสข้อความบนกระดาษของเขา

โดยเขาจะเปลี่ยนทุกตัวสระ (a, e, i, o, u) โดยเขียนด้วยสระตัวนั้นก่อน แล้วตามด้วยตัวอักษร p แล้วตามด้วยสระตัวเดิมนั้นอีกครั้ง

ตัวอย่างเช่นคำว่า "computer" จะกลายเป็น "copompuputeper"

และคำว่า "paprika" จะกลายเป็น "papapripikapa"

แต่อาจารย์ก็มาหาเขา และยึดกระดาษที่เขียนข้อความที่เข้ารหัสแล้ว ซึ่งอาจยังเข้ารหัสไม่สมบูรณ์ก็ได้ และต้องการที่จะถอดหาข้อความเดิมออกมา

จงเขียนโปรแกรมที่รับข้อความที่เข้ารหัสของลูคัส และพิมพ์ข้อความก่อนเข้ารหัสออกมา

ข้อมูลเข้า
บรรทัดเดียว เป็นข้อความที่ถูกเข้ารหัส ข้อความจะประกอบด้วย ตัวอักษร a - z ตัวเล็ก และช่องว่าง โดยจะไม่มีช่องว่างที่หัวหรือท้ายข้อความ จำนวนตัวอักษรทั้งหมดไม่เกิน 100 ตัวอักษร

ข้อมูลออก
บรรทัดเดียว เป็นข้อความก่อนที่ลูคัสจะเข้ารหัส

ตัวอย่างข้อมูลเข้า/ข้อมูลออก
ข้อมูลเข้า	                                                      ข้อมูลออก
copompuputeper papapripikapa	                               computer paprika
bapas jepe doposapadnapa opovapa kepemipijapa	               bas je dosadna ova kemija'''
sala = 'aeiou'
encode = input()
decode = ""
i = 0
while i < len(encode):
    if i + 2 < len(encode) and encode[i] in sala and encode[i + 1] == 'p' and encode[i + 2] == encode[i]:
        decode += encode[i]
        i += 3
    else:
        decode += encode[i]
        i += 1
print(decode)
        
    