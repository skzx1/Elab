'''เมนู
ร้านอาหาร fast food แห่งหนึ่งมีรายการอาหารในเมนูหลักให้เลือกรับประทาน 3 เมนู คือ
<B>urger Meal
<C>hicken Meal
<P>asta Meal
และในแต่ละเมนูหลักมีเมนูย่อยพร้อมราคา ดังนี้

<B>urger Meal ประกอบด้วยเมนูย่อย

<R>egular Burger 60 บาท
<C>heese Burger 75 บาท
<D>ouble Cheese Burger 90 บาท
<C>hicken Meal ประกอบด้วยเมนูย่อย

<F>ried Chicken 120 บาท
<G>rilled Chicken 150 บาท
<C>hef's Chicken 180 บาท
<P>asta Meal ประกอบด้วยเมนูย่อย

<S>paghetti de Italiano 90 บาท
<L>asagna Supreme 120 บาท
<M>acaroni Special 100 บาท
จงเขียนโปรแกรมเพื่อแสดงเมนูหลัก ดังนี้


[hide line #]
---<< Main Menu >>---
    <B>urger Meal
    <C>hicken Meal
    <P>asta Meal
แล้วรับตัวอักษร ‘B’, ‘C’ หรือ ‘P’ สําหรับเมนูหลัก และในแต่ละเมนูหลักให้แสดงเมนูย่อย เช่น ถ้าเลือกเมนู ‘B’ ให้แสดงเมนูย่อย ดังนี้


[hide line #]
---<< Burger Sub Menu >>---
    <R>egular Burger
    <C>heese Burger
    <D>ouble Cheese Burger
จากนั้นให้รับตัวอักษรของแต่ละเมนูย่อย เมื่อผู้ใช้เลือกเมนูย่อยเรียบร้อยแล้วให้แสดงราคาของรายการอาหารที่ผู้ใช้เลือก
โดยใช้ข้อความ “Your ชื่อเมนูย่อย is xx Baht.” (เมื่อ xx เป็นราคาของเมนูย่อยนั้นๆ)

หมายเหตุ ให้แสดงข้อความ “Invalid main menu choice.” หรือ “Invalid sub menu choice.” เมื่อเลือกเมนูหลักหรือเมนูย่อยของแต่ละเมนูหลักไม่ถูกต้อง
รวมถึงให้รองรับกรณีป้อนเมนูทั้งตัวพิมพ์เล็กและตัวพิมพ์ใหญ่

ตัวอย่าง Input/Output

[hide line #]
---<< Main Menu >>---
    <B>urger Meal
    <C>hicken Meal
    <P>asta Meal
Enter your choice: B
---<< Burger Sub Menu >>---
    <R>egular Burger
    <C>heese Burger
    <D>ouble Cheese Burger
Enter your choice: D
Your Double Cheese Burger is 90 Baht.'''
print("---<< Main Menu >>---")
print("    <B>urger Meal") 
print("    <C>hicken Meal")
print("    <P>asta Meal")
main = input("Enter your choice: ")
if main == 'B' or main == 'b':
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    #sub1
    sub = input("Enter your choice: ")
    if sub == 'R' or sub == 'r':
        print("Your Regular Burger is 60 Baht.")
    elif sub == 'C' or sub == 'c':
        print("Your Cheese Burger is 75 Baht.")
    elif sub == 'D' or sub == 'd':
        print("Your Double Cheese Burger is 90 Baht.")
    else:
        print("Invalid sub menu choice.")
#main2
elif main == 'C' or main == 'c':
    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")
     #sub2
    sub = input("Enter your choice: ")
    if sub == 'F' or sub == 'f':
        print("Your Fried Chicken is 120 Baht.")
    elif sub == 'G' or sub == 'g':
        print("Your Grilled Chicken is 150 Baht.")
    elif sub == 'C' or sub == 'c':
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print("Invalid sub menu choice.")
#main3
elif main == 'P' or main == 'p':
    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")
    #sub3
    sub = input("Enter your choice: ")
    if sub == 'S' or sub == 's':
        print("Your Spaghetti de Italiano is 90 Baht.")
    elif sub == 'L' or sub == 'l':
        print("Your Lasagna Supreme is 120 Baht.")
    elif sub == 'M' or sub == 'm':
        print("Your Macaroni Special is 100 Baht.")
    else:
        print("Invalid sub menu choice.")
else:
    print("Invalid main menu choice.")        
