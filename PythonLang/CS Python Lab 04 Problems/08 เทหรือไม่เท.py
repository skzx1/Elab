'''เทหรือไม่เท
อาจารย์สอนชั้นประถมที่ 5 พร้อมใจกันให้การบ้านเด็กๆ เด็กน้อยที่ขยันไม่มากคนหนึ่งใช้เวลาไม่มากนักในการสร้างกติกาเพื่อตัดสินใจว่าจะทำการบ้านหรือไม่ ดังนี้

ถ้าเหลือเวลาน้อยกว่า 2 วันก่อนถึงกำหนดส่งการบ้าน เด็กน้อยตัดสินใจทุ่ม (?) เททำการบ้านให้เสร็จ
ถ้าเหลือเวลามากกว่า 5 วันก่อนถึงกำหนดส่งการบ้าน เด็กน้อยตัดสินใจเท
มิเช่นนั้น ถ้าอุณหภูมิสูงกว่า 40 องศาเซลเซียส หรือ ถ้าอุณหภูมิสูงกว่า 25 องศาเซลเซียส และฝนตก เด็กน้อยตัดสินใจเท
กำหนดข้อมูลนำเข้าประกอบด้วยจำนวนนาทีก่อนถึงกำหนดส่งการบ้าน (โดยระยะเวลาตั้งแต่ครึ่งวันขึ้นไปให้คิดเป็น 1 วัน) อุณหภูมิ และสถานะฝนตก (Y หรือ N) แล้วแสดงผลจำนวนวันก่อนถึงกำหนดส่งงานหร้อมผลการตัดสินใจ

ตัวอย่าง 1

Minutes before due: 65002
Temperature: 38
Is it raining (y/n)? Y
>>> 45 days before due.
>>> I will not do the assignment.
ตัวอย่าง 2

Minutes before due: 6000
Temperature: 20.5
Is it raining (y/n)? n
>>> 4 days before due.
>>> I will do the assignment.'''
minute = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = str(input("Is it raining (y/n)? "))
days = minute / (60 * 24)

if (days - int(days) >= 0.5):
    days = int(days) + 1
else:
    days = int(days)
    
if (days < 2):
   dc = ">>> I will do the assignment."
elif (temp > 40 or (temp > 25 and (rain == "y" or rain == "Y"))):
    dc = ">>> I will not do the assignment."
elif (days > 5): 
    dc = ">>> I will not do the assignment."
else: 
    dc = ">>> I will do the assignment."

print(f">>> {days} days before due.")
print(dc)
