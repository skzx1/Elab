'''Alternating Sum
Alternating Sum คือ ผลรวมของตัวเลขในลำดับที่สลับกันระหว่างจำนวนเต็มบวกและจำนวนเต็มลบของจำนวนที่เพิ่มขึ้น

เช่น Alternating Sum ของ 10 จำนวนแรก คือ 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10 = -5

Alternating Sum ของ 15 จำนวนแรก คือ 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10 + 11 - 12 + 13 - 14 + 15 = 8

เขียนโปรแกรมเพื่อหา Alternating Sum ของ n ตัวแรก เมื่อ n เป็นจำนวนเต็มบวก

ตัวอย่าง Input/Output 1

Enter n of series: 10
Alternating Sum from 1 to 10 is -5
ตัวอย่าง Input/Output 2

Enter n of series: 15
Alternating Sum from 1 to 15 is 8'''
def Alternative(n):
     sum = 0
     while n > 0:
        if n % 2 == 0:
            sum -= n
        else:
            sum += n
        n -= 1
     return sum

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n, Alternative(n)))
