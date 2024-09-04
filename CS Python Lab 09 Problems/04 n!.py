'''n!
เขียนฟังก์ชันและเรียกฟังก์ชัน เพื่อคำนวณค่า factorial ของจำนวนเต็ม n หรือ n! โดย n มีค่ามากกว่าหรือเท่ากับ 0

ตัวอย่าง Input/Output 1

Enter n: 6
6! = 720
ตัวอย่าง Input/Output 2

Enter n: 1
1! = 1

'''
def factorial(n):
     i = 0
     while i <= n:
          j = i
          fac = 1
          while j > 0:
               fac *= j
               j -= 1     
          i += 1
     return fac
n = int(input("Enter n: "))
print(f"{n}!", "=", "=",)
