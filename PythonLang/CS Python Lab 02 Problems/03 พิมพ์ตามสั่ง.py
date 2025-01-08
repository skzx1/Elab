'''พิมพ์ตามสั่ง
เขียนโปรแกรมเพื่อรับจำนวนจริงสองจำนวน คือ inc และ ex แล้วพิมพ์ข้อความตามรูปแบบต่อไปนี้

ตัวอย่าง Output
(สมมติรับ input เป็น 145.67 และ -20.25 ตามลำดับ)

123456789012345678901234567890
Total Income  +145.67 bahts
Expense        -20.25 bahts
Profit       00125.42 bahts
ตัวอย่าง Output
(สมมติรับ input เป็น 2000.3 และ -2.25 ตามลำดับ)

123456789012345678901234567890
Total Income +2000.30 bahts
Expense         -2.25 bahts
Profit       01998.05 bahts
(ผลลัพธ์ต้องการให้จุดทศนิยมตรงกัน)'''
inc = float(input())
ex = float(input())
total = inc + ex
print("1234567890" * 3)
print(f"Total Income {'':>0}{inc:>+8.2f} bahts")
print(f"Expense {'':>5}{ex:>8.2f} bahts")
print(f"Profit{'':>7}{total:>08.2f} bahts")