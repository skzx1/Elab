'''Pyramid Builder
เขียนโปรแกรมเพื่อสร้างพิระมิด (Pyramid) ตามจำนวนชั้นที่รับเข้ามา

ข้อมูลเข้า
จำนวนชั้นของหอคอย เป็นจำนวนเต็มบวกเสมอ

ข้อมูลออก
แสดงพิระมิด โดยแต่ละชั้นจะใช้ * แทนบล็อกที่ใช้ในการสร้างพิระมิด

ตัวอย่างข้อมูลเข้า/ข้อมูลออก
ข้อมูลเข้า	ข้อมูลออก
10	
|         *         |
|        ***        |
|       *****       |
|      *******      |
|     *********     |
|    ***********    |
|   *************   |
|  ***************  |
| ***************** |
|*******************|
5	
|    *    |
|   ***   |
|  *****  |
| ******* |
|*********|'''
layer = int(input())
for i in range(layer):
    print(f"|{' '*(layer-i-1)}{'*'*(2*i+1)}{' '*(layer-i-1)}|")
    
   