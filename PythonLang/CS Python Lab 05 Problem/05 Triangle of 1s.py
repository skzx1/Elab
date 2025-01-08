'''จงเขียนโปรแกรมเพื่อรับจำนวนเต็มที่มีค่ามากกว่าหรือเท่ากับศูนย์เพื่อแสดงจำนวนบรรทัดของผลลัพธ์ แล้วแสดงผลตามตัวอย่าง

ตัวอย่าง 1

Enter height: 5
        1
      1   1
    1       1
  1           1
1               1
ตัวอย่าง 2

Enter height: 1
1'''
height = int(input("Enter height: "))
s = 3
i = 1

while height > 0:
    if i == 1:
        print(" " * (2 * (height - 1)) + "1")
    else:
        print(" " * (2 * (height - 1)) + "1" + " " * s + "1")
        s += 4
    height -= 1    
    i += 1