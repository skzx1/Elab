านขายพิซซา
ให้ผู้เรียนเขียนโปรแกรมสำหรับร้านขายพิซซาซึ่งขายพิซซาสามขนาด ได้แก่ ขนาดเล็ก กลาง และใหญ่ ตามขนาดเส้นผ่านศูนย์กลาง (diameter) 10 (ขนาด s), 16 (ขนาด m), และ 20 (ขนาด l) นิ้ว ตามลำดับ โดยผู้ใช้สามารถเลือกเพิ่มเพิ่มเปปเปอโรนี (pepperoni) ชีส (cheese) และ/หรือเห็ด (mushroom) บนหน้าพิซซาได้ โดยทางร้านกำหนดราคาขาย (price) เป็น 1.5 เท่าของต้นทุน ดังสมการ
price
=
1.5
×
cost
โดยที่ต้นทุนของพิซซาแต่ละถาดจะคำนวณจากสูตร
cost
=
fixedcost
+
(
basecost
×
area
)
+
(
extracost
×
area
)
ร้านได้กำหนดให้ fixedcost และ basecost มีค่าเท่ากับ 5 และ 2 บาทตามลำดับ ส่วนค่า extracost จะมีค่าเป็น 0 หากผู้ใช้ไม่ต้องการเพิ่มเครื่องปรุงอะไรเลย แต่การเลือกเพิ่มเครื่องปรุงแต่ละชนิดจะทำให้ extracost มีความเปลี่ยนแปลงดังต่อไปนี้

การเพิ่ม pepperoni จะทำให้ extracost เพิ่มขึ้น 0.5 บาท
การเพิ่ม cheese จะทำให้ extracost เพิ่มขึ้น 0.25 บาท
การเพิ่ม mushroom จะทำให้ extracost เพิ่มขึ้น 0.30 บาท
ส่วนค่า area นั้นจะคำนวนจากสูตร
a
r
e
a
=
π
×
(
diameter
)
2
/
4
ซึ่งเวลาเขียนโปรแกรมให้ส่ง #include <math.h> แล้วใช้ค่าคงที่ M_PI แทนค่าพาย

ตัวอย่างผลลัพธ์ที่ 1
Welcome to My Pizza Shop!!
~~~~~~~~~~~~~~~~~~~~~~~~~~
Enter pizza size (1=s, 2=m, or 3=l): 2
Extra pepperoni? (1=yes, 0=no): 1
Extra cheese? (1=yes, 0=no): 0
Extra mushroom? (1=yes, 0=no): 0
~~~~~~~~~~~~~~~~~~~~~~~~~~
Your order costs 761.48 baht.
Thank you.
ตัวอย่างผลลัพธ์ที่ 2
Welcome to My Pizza Shop!!
~~~~~~~~~~~~~~~~~~~~~~~~~~
Enter pizza size (1=s, 2=m, or 3=l): 1
Extra pepperoni? (1=yes, 0=no): 0
Extra cheese? (1=yes, 0=no): 1
Extra mushroom? (1=yes, 0=no): 0
~~~~~~~~~~~~~~~~~~~~~~~~~~
Your order costs 272.57 baht.
Thank you.

[hide line #]
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    char sizein[4], pepin[4], chein[4], mushin[4];
    int size, pepperoni, cheese, mushroom, diameter, fixedcost = 5, basecost = 2;
    float cost, area, price, extracost = 0;
    printf("Welcome to My Pizza Shop!!\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    
    printf("Enter pizza size (1=s, 2=m, or 3=l): ");
    fgets(sizein, 4, stdin);
    size = atoi(sizein);
    
    printf("Extra pepperoni? (1=yes, 0=no): ");
    fgets(pepin, 4, stdin);
    pepperoni = atoi(pepin);
    
    printf("Extra cheese? (1=yes, 0=no): ");
    fgets(chein, 4, stdin);
    cheese = atoi(chein);
    
    printf("Extra mushroom? (1=yes, 0=no): ");
    fgets(mushin, 4, stdin);
    mushroom = atoi(mushin);
    
    if(size == 1){
        diameter = 10;
    }else if(size == 2){
        diameter = 16;
    }else if(size == 3){
        diameter = 20;
    }
    area = M_PI * diameter * diameter / 4;
    if (pepperoni == 1){
        extracost += 0.5;
    }else{
        extracost = extracost;
    }
    if (cheese == 1){
        extracost += 0.25;
    }else{
        extracost = extracost;
    }
    if (mushroom == 1){
        extracost += 0.30;
    }else{
        extracost = extracost;
    }

    cost = fixedcost + (basecost * area) + (extracost * area);
    price = cost * 1.5;
    printf("~~~~~~~~~~~~~~~~~~~~~~~~~~\nYour order costs %.2f baht.\nThank you.", price);
    return 0;
}