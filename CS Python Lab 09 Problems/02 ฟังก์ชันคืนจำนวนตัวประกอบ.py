'''ฟังก์ชันคืนจำนวนตัวประกอบ
ให้เขียนฟังก์ชัน factor_count(n) ที่คืนจำนวนของตัวประกอบของ จำนวนเต็มบวก n

จำนวนเต็มบวกที่หาร n ลงตัว เรียกว่า ตัวประกอบของ n

Example 1
Enter n: 5
2
Example 2
Enter n: 70
8
ตัวประกอบของ 70 มี 8 ตัว คือ 1, 2, 5, 7, 10, 14, 35 และ 70'''
def factor_count(n):
 i = 1
 c = 0 
 while i <= n:
      if n % i == 0:
          c += 1
      i += 1
 return c
'''
[hide line #]
ส่วนของโปรแกรมหลักที่เรียกใช้ฟังก์ชันดังกล่าว เป็นดังด้านล่าง


[hide line #]
n = int(input("Enter n: "))
c = factor_count(n)
print(c)'''