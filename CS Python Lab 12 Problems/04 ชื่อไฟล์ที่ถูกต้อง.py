'''ชื่อไฟล์ที่ถูกต้อง
ระบบปฏิบัติการหนึ่งกำหนดชื่อไฟล์ที่ถูกต้องไว้ดังนี้

ความยาวสูงสุดของชื่อไฟล์คือ 15 ตัวอักษร
ความยาวสูงสุดของนามสกุลไฟล์คือ 3 ตัวอักษร
มีเครื่องหมาย . ได้อันเดียว คืออันที่คั่นระหว่างชื่อกับนามสกุลไฟล์ (อันสุดท้าย)
ห้ามใช้เครื่องหมาย \ / * : | " < > ในการตั้งชื่อไฟล์
ห้ามมีช่องว่างในชื่อไฟล์
ให้นิสิตเขียนโปรแกรมรับชื่อไฟล์จากผู้ใช้แล้วปรับชื่อไฟล์ให้ถูกต้องตามข้อกำหนด โดย

เปลี่ยนช่องว่างให้เป็น _
เปลี่ยนอักขระต้องห้ามให้เป็น _
เปลี่ยน . ให้เป็น _ ยกเว้นอันสุดท้าย
ตัดชื่อและนามสกุลไฟล์ให้มีความยาวไม่เกินที่กำหนด
ถ้าไฟล์ไม่มีนามสกุลก็ไม่ต้องใส่นามสกุลและไม่ต้องใส่ . ตัวสุดท้าย
ตัวอย่างข้อมูลเข้า/ข้อมูลออก

ข้อมูลเข้า	ข้อมูลออก
a.b.c.d.e	a_b_c_d.e
abcdefghijklmnop.qrstuv	abcdefghijklmno.qrs
*$ 7h|$_to<>:dif.\/.g|od	_$_7h_$_to___di.g_o
Is this too difficult?	Is_this_too_dif'''
filename = input()
no = r'''\ / * : | " < >''' 
filename = filename.replace(' ', '_')
for i in no:
    filename = filename.replace(i,'_')
dot = filename.rfind('.')
if dot != -1:
    name = filename[:dot]
    sur = filename[dot+1:]
    name = name.replace('.', '_')
    name = name[:15]
    sur = sur[:3]
    filename = name + '.' + sur
else:
    filename = filename[:15]
print(filename)
