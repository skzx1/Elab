'''Prime number checker
จำนวนเฉพาะ (prime number หรือเรียกสั้นๆว่า prime) เป็นจำนวนเต็มบวกซึ่งมีตัวหารเพียงสองตัวคือ 1 และตัวมันเอง
ตัวอย่างเช่น 7 เป็นจำนวนเฉพาะเนื่องจากเลขที่หารมันลงตัวมีเพียง 1 และ 7
ส่วน 10 ไม่ใช่จำนวนเฉพาะ เพราะมีตัวหารถึง 4 ตัว คือ 1, 2, 5 และ 10
จะเห็นว่าจากนิยามของจำนวนเฉพาะจะได้ว่า 1 ไม่ใช่จำนวนเฉพาะเนื่องจากมีตัวหารเพียงตัวเดียวคือ 1

ให้เขียนโปรแกรมเพื่อรับจำนวนเต็มบวก number และตรวจสอบว่า number เป็นจำนวนเฉพาะหรือไม่ โดยให้โปรแกรมสามารถรับจำนวนเต็มจนกว่าผู้ใช้จะป้อนค่า 0

หมายเหตุ ให้แสดงข้อความแจ้งข้อความโต้ตอบหรือข้อผิดพลาดที่อาจเกิดขึ้นในกรณีต่างๆ ดังนี้

"End of program, goodbye." เมื่อจำนวนเต็มที่รับเข้ามา มีค่าเท่ากับ 0 แล้วจบโปรแกรมทันที
"Invalid input, try again." เมื่อจำนวนเต็มที่รับเข้ามา มีค่าน้อยกว่าหรือเท่ากับ 1 แล้วให้ป้อนค่าใหม่
ตัวอย่างผลลัพธ์ที่ 1
Enter a number: 17
17 is a prime number.
Enter a number: 25
25 is not a prime number.
Enter a number: 1
Invalid input, try again.
Enter a number: 119
119 is not a prime number.
Enter a number: 0
End of program, goodbye.'''
while True:
  x = int(input("Enter a number: "))
  if x == 0:
    print("End of program, goodbye.")
    break
  elif x <= 1:
    print("Invalid input, try again.")    
  else:
    i = 2
    while  i <= x/2:
      if x % i == 0:    
          print(f"{x} is not a prime number.")
          break
      i+=1  
    else:
      print(f"{x} is a prime number.")
