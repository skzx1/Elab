num = input("ข้อมูลเข้า: ")  # รับข้อมูลจากผู้ใช้
valid = True  # ตัวแปรเพื่อตรวจสอบความถูกต้องของรูปแบบ

# ตรวจสอบรูปแบบตัวเลข
for i in num:
    if i not in '0123456789.,':  # ตรวจสอบว่าตัวอักษรใน num อยู่ในกลุ่มที่กำหนด
        valid = False
        break

if not valid:  # ถ้าตรวจพบว่ามีอักขระที่ไม่ถูกต้อง
    print('ERROR')
else:
    # ตัดเครื่องหมาย ',' ออก
    num = num.replace(',', '')

    # ตรวจสอบจำนวนจุดทศนิยม
    if '.' in num:
        dot_index = num.find('.')
        if num.count('.') > 1 or len(num) - dot_index != 3:  # ตรวจสอบว่าเป็นจุดทศนิยมสองตำแหน่งหรือไม่
            print('ERROR')
        else:
            # เพิ่มค่า 1 และแสดงผลลัพธ์
            print(f"{float(num) + 1:.2f}")
    else:
        # ถ้าไม่มีจุดทศนิยมให้แสดงผลลัพธ์เป็นจำนวนเต็ม
        print(int(num) + 1)
