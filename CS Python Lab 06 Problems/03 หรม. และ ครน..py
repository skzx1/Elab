'''จงเขียนโปรแกรมเพื่อรับจำนวนเต็มที่มีค่ามากกว่าศูนย์ 2 จำนวน และแสดงผลลัพธ์เป็นตัวหารร่วมมาก (Great Common Divisor: GCD) และจำนวนที่เป็นตัวคูณร่วมน้อย (Least Common Multiplier: LCM) ของจำนวนทั้งสอง โดยใช้วิธีของ Euclid’s ดังนี้

การหา หรม.:

หาเศษที่ได้จากการหารจำนวนที่มากกว่าด้วยจำนวนที่น้อยกว่า
แทนจำนวนที่มากกว่าด้วยจำนวนที่น้อยกว่า และแทนจำนวนที่น้อยกว่าด้วยเศษที่ได้จากข้อที่แล้ว
ทำซ้ำกระบวนการข้างต้นจนกระทั่งจำนวนที่น้อยกว่ามีค่าเป็น 0 จะได้คำตอบคืออีกจำนวนที่ไม่เป็น 0
ตัวอย่าง
gcd(20, 8) -> 20 mod 8 มีค่าเท่ากับ 4
แทนที่ 20 ด้วย 8 และแทนที่ 8 ด้วย 4
gcd(8, 4) -> 8 mod 4 มีค่าเท่ากับ 0
แทนที่ 8 ด้วย 4 และแทนที่ 4 ด้วย 0
ดังนั้นจะได้ว่า หรม. ของ 20 และ 8 มีค่าเท่ากับ 4

การหา ครน.:
พิจารณาตัวประกอบเฉพาะของ 20 และ 8 พบว่า
20 = 2 * 2 * 5
8 = 2 * 2 * 2
จะได้ว่า หรม. ของ 20 และ 8 คือ 2 * 2 และ ครน. ของ 20 และ 8 คือ 2 * 2 * 2 * 5 ซึ่งจะเห็นได้ว่า เราสามารถหา ครน. จาก หรม. ได้

ตัวอย่างโปรแกรม

Enter the first number: 20
Enter the second number: 8
  >> gcd(20, 8) =      4
  >> lcm(20, 8) =     40'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
a = num1
b = num2

while b:
    a, b = b, a % b
gcd = a
lcm = (num1 * num2) // gcd

print(f"  >> gcd({num1}, {num2}) = {gcd:6}")
print(f"  >> lcm({num1}, {num2}) = {lcm:6}")