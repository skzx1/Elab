'''เติมน้ำมัน
แก้วกับขวัญพักอยู่ที่คอนโดเดียวกันและเพิ่งซื้อรถใหม่มาคนละคันเป็นรถยี่ห้อเดียวกันรุ่นเดียวกันเหมือนกันทุกอย่าง รถรุ่นนี้เป็นอีโคคาร์จึงสามารถเดินทางได้ถึง 15 กิโลเมตรต่อน้ำมัน 1 ลิตร

แต่แก้วเป็นคนขี้กังวลจึงเลือกที่จะเติมน้ำมันเมื่อปริมาณน้ำมันรถเหลือ 50% ของความจุถัง ในขณะที่ขวัญเป็นคนที่ชอบความท้าทายจึงเติมน้ำมันเมื่อปริมาณเหลือ 10% ของความจุถัง เมื่อน้ำมันลดถึงจุดที่กำหนดทั้งแก้วและขวัญจะเติมน้ำมันทันทีแม้ว่าจะถึงจุดหมายแล้ว

เพื่อฉลองรถใหม่แก้วกับขวัญใช้รถของตนเองออกเดินทางไปยังจุดหมายที่ใช้ระยะทางเท่ากัน โดยทั้งสองคนจะเติมน้ำมันครั้งแรกที่ปั๊มที่อยู่ติดกับคอนโดจนเต็มถังไม่ว่ารถจะมีน้ำมันเหลือเท่าไหร่ แต่การเติมน้ำมันครั้งต่อๆ ไปจะเป็นไปตามข้อกำหนดที่กล่าวไว้ ทั้งสองคนมีน้ำมันสำรองที่พร้อมจะเติมเสมอ

ให้นิสิตเขียนโปรแกรมรับข้อมูลเลขจำนวนเต็มตัวแรกคือระยะทางที่แก้วกับขวัญเดินทางเป็นกิโลเมตร
และในบรรทัดต่อไปเป็นความจุของถังน้ำมันเป็นลิตรซึ่งเป็นเลขจำนวนเต็มเช่นกัน
จากนั้นให้พิมพ์จำนวนครั้งที่แก้วและขวัญต้องเติมน้ำมันในการเดินทางไปถึงจุดหมาย (รวมการเติมครั้งแรกด้วย)
โดยพิมพ์ของแก้วก่อนในบรรทัดแรกและตามด้วยของขวัญในบรรทัดที่สอง จำนวนครั้งที่เติมน้ำมันต้องเป็นเลขจำนวนเต็ม

ตัวอย่างข้อมูลเข้า/ข้อมูลออก
ข้อมูลเข้า	ข้อมูลออก
400        6
10	       3
540
12	       7
           4'''
distance = int(input())
tankcap = int(input())

gaew = tankcap * 0.5
gaew_refill = (tankcap - gaew) * 15
gtotal_refill = (distance // gaew_refill) + 1  

kwan = tankcap * 0.1
kwan_refill = (tankcap - kwan) * 15
ktotal_refill = (distance // kwan_refill) + 1

print(int(gtotal_refill))
print(int(ktotal_refill))