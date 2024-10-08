'''name, name & name
จงเขียนฟังก์ชัน namelist(names) ที่รับ parameter names ซึ่งเป็น list ของชื่อคนซึ่งเป็น string

โดยฟังก์ชัน namelist(names) นี้ จะต้องคืนค่า string ที่เป็นข้อความที่เชื่อมทุกชื่อคนใน list ด้วย , ยกเว้นคู่สุดท้าย ให้เชื่อมด้วย & (ไม่มีช่องว่างหน้าเครื่องหมาย , แต่มีช่องว่างหลังเครื่องหมาย , หน้าเครื่องหมาย & และหลังเครื่องหมาย &)

ตัวอย่างผลลัพธ์เมื่อเรียกฟังก์ชัน

print( namelist(['Bart', 'Viola', 'Peter', 'Nostel']) )

Bart, Viola, Peter & Nostel
print( namelist(['Bart', 'Viola']) )

Bart & Viola
print( namelist(['Peter']) )

Peter
print( namelist([]) == '' )

True
ส่งเฉพาะ Function Definition ของ namelist(names)'''
def namelist(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 0:
        return ''
    else:
        return ', '.join(names[:-1]) + ' & ' + names[-1]

print( namelist([]) == '' )
