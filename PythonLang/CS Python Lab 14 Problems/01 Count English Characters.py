'''Count English Characters
จงเขียนฟังก์ชัน count_char(word) ซึ่งรับสตริง word เข้ามา แล้วสร้าง dictionary เพื่อนับจํานวนครั้งที่ตัวอักขระปรากฏในสตริง word

โดยจะนับทั้งอักขระภาษาอังกฤษตัวเล็กและตัวใหญ่รวมกัน แต่ใน dictionary จะใช้เป็นอักขระภาษาอังกฤษตัวเล็กในการนับ

และไม่สนใจอักขระอื่นใด เช่น ช่องว่าง หรือเครื่องหมาย

หมายเหตุ ห้ามใช้คำสั่ง count

ให้ส่งคำตอบเฉพาะ definition ของ function count_char(word)

ตัวอย่างผลลัพธ์เมื่อเรียกฟังก์ชัน count_char
 
>>> print(count_char('Hello, There'))
{'h': 2, 'e': 3, 'l': 2, 'o': 1, 't': 1, 'r': 1}'''
def count_char(word):
    asw = {}
    for i in word:
        i = i.lower()
        if i.isalpha():
            if i in asw:
                asw[i] += 1
            else:
                asw[i] = 1
    return asw