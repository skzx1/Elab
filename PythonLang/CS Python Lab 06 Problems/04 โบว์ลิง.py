'''การโยนโบว์ลิง 1 เกมประกอบด้วยการโยนทั้งหมด 10 frames แต่ละ frame ผู้เล่นจะโยนลูกโบว์ลิง 1 หรือ 2 ลูก เพื่อล้ม pin จำนวน 10 pins ที่ปลายราง ผลจากการโยนในแต่ละ frame มีดังนี้

การล้ม pin ทั้ง 10 ด้วยบอลลูกแรก เรียกว่า strike และไม่ต้องโยนบอลลูกที่สอง
การล้ม pin ทั้ง 10 ด้วยบอลทั้งสองลูก (รวมจำนวน pin จากการโยน 2 ครั้ง) เรียกว่า spare
การโยนบอลครบ 2 ลูกแล้วยังไม่สามารถล้ม pin ได้ครบ 10 pin เรียกว่า open frame
ทั้งนี้ ในการคิดคะแนนในแต่ละเฟรม ทั้ง strike และ spare คิดเป็น 10 แต้ม และ open frame ได้แต้มตามจำนวน pin ล้ม

เขียนโปรแกรมเพื่อรับแต้มจากการโยนโบว์ลิงทั้ง 10 frames และแสดงคะแนนที่ได้จากเกมนั้น

ตัวอย่างโปรแกรม

Frame # 1
  Number of pins down: 10
Frame # 2
  Number of pins down: 7
Frame # 2
  Number of pins down (0-3): 0
Frame # 3
  Number of pins down: 9
Frame # 3
  Number of pins down (0-1): 1
Frame # 4
  Number of pins down: 7
Frame # 4
  Number of pins down (0-3): 1
Frame # 5
  Number of pins down: 10
Frame # 6
  Number of pins down: 10
Frame # 7
  Number of pins down: 0
Frame # 7
  Number of pins down (0-10): 5
Frame # 8
  Number of pins down: 6
Frame # 8
  Number of pins down (0-4): 3
Frame # 9
  Number of pins down: 1
Frame # 9
  Number of pins down (0-9): 8
Frame # 10
  Number of pins down: 1
Frame # 10
  Number of pins down (0-9): 8
Total score is 87'''
frame = 1
p = 0
while True:
    if frame > 10:
        break
    print(f"Frame # {frame}")
    x = int(input("  Number of pins down: "))
    if x == 10:
        frame+=1
        p += 10
    else:
        p += x
        print(f"Frame # {frame}")
        y = int(input(f"  Number of pins down (0-{10-x}): "))
        p += y
        frame+=1

print(f"Total score is {p}")
        