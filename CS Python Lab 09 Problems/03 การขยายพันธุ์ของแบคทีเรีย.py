'''การขยายพันธุ์ของแบคทีเรีย
ในการศึกษาวิจัยการขยายพันธุ์ของแบคทีเรียสายพันธุ์ bal-x บนอาหาร พบว่า ในแต่ละวันจะมีแบคทีเรียสายพันธุ์ bal-x จะขยายจำนวนเพิ่มขึ้นจากเดิมวันละ d% จากเดิม และทำปฏิกิริยากับแบคทีเรียอื่นในอากาศเพิ่มอีก aug ตัว

เช่น หากเริ่มต้นมีแบคทีเรีย bal-e (หนึ่งในสายพันธุ์ของ bal-x) อยู่ 1000 ตัว มีอัตราการขยายตัววันละ 2.0% และทำปฏิกิริยากับแบคทีเรียอื่นเพิ่มขึ้นวันละ 30 ตัว
เมื่อผ่านไป 1 วัน แบคทีเรีย bal-e จะมีจำนวนเพิ่มขึ้นเป็น 1000 + 1000 * 0.02 + 30 = 1050 ตัว
เมื่อผ่านไป 2 วัน แบคทีเรีย bal-e จะมีจำนวนเพิ่มขึ้นเป็น 1050 + 1050 * 0.02 + 30 = 1101 ตัว
เมื่อผ่านไป 3 วัน แบคทีเรีย bal-e จะมีจำนวนเพิ่มขึ้นเป็น 1101 + 1101 * 0.02 + 30 = 1153 ตัว (จำนวนแบคทีเรียเป็นจำนวนเต็มเสมอ)

นักวิจัยมีข้อมูลจำนวนแบคทีเรียเริ่มต้น (p0) อัตราการขยายตัวของแบคทีเรียต่อวัน (percent)% จำนวนแบคทีเรียที่เพิ่มขึ้นเมื่อทำปฏิกิริยากับแบคทีเรียในอากาศ (aug จำนวนอาจลดลง หรือเป็น 0 ก็ได้)

นักวิจัยต้องการทราบว่า จะต้องใช้จำนวนกี่วันนับจากวันแรกที่แบคทีเรียสายพันธุ์นี้ จะมีจำนวนมากกว่าหรือเท่ากับ p

ในข้อนี้ ให้เขียนฟังก์ชัน nb_year(p0, percent, aug, p) เพื่อคืนค่าจำนวนวัน นับจากวันแรกที่แบคทีเรียสายพันธุ์นี้ขยายพันธุ์จนมีจำนวนมากกว่าหรือเท่ากับ p

ตัวอย่างการเรียกฟังก์ชัน
print( nb_year(1000, 2, 30, 1150) )

3
print( nb_year(1500000, 0.25, 1000, 2000000) )

94
ส่งคำตอบเฉพาะ Function Definition ของ nb_year(p0, percent, aug, p)


'''
def nb_year(p0, percent, aug, p):
    i = 0
    day = p0
    while day < p:
        day = int(day + day * percent/100 + aug)
        i += 1
    return i
