'''ทอนเงิน (ฟังก์ชัน)
ให้นิสิตเขียนฟังก์ชันชื่อ change ที่จะรีเทิร์นจำนวนธนบัตรที่แลกเงินได้ ไม่ว่าจะเป็นเงินจำนวนเท่าไหร่หรือธนบัตรมูลค่าเท่าใด

เช่นจำนวนเงิน 45 บาทจะแลกธนบัตรใบละ 20 บาทได้ 2 ใบ (ฟังก์ชันนี้จะไม่สนใจเศษเงินที่เหลือ)
ในขณะที่จำนวนเงิน 120 บาทจะแลกธนบัตรใบละ 100 บาทได้ 1 ใบ

จากนั้นให้เติมโปรแกรมให้สมบูรณ์ โดยโปรแกรมจะรับจำนวนเงินเข้ามา และคำนวณว่าจะแลกเป็นธนบัตร 500, 100, 20, 5, และ 1 บาทได้กี่ใบ โดยกำหนดว่าจะแลกเงินเป็นธนบัตรที่มีค่ามากที่สุดก่อน และธนบัตรมีแลกได้ไม่จำกัดจำนวน โปรแกรมนี้ต้องใช้ฟังก์ชันที่นิสิตนิยาม

ตัวอย่าง
Enter total money: 1218
500: 2
100: 2
 20: 0
  5: 3
  1: 3'''
def change(money):
    mo = money // 500
    money = money % 500
    mo = money // 100
    money = money % 100
    mo = money // 20
    money = money % 20
    mo = money // 5
    money = money % 5
    mo = money // 1
    return mo
left = 0
money = int(input("Enter total money: "))
b500 = change(money)
left = left - b500  * 500
b100 = change(money)
left = left - b100  * 100
b20 = change(money)
left = left - b20  * 20
b5 = change(money)
left = left - b5  * 5
b1 = change(money)
left = left - b1  * 1

print(f"500: {b500}")
print(f"100: {b100}")
print(f" 20: {b20}")
print(f"  5: {b5}")
print(f"  1: {b1}")





