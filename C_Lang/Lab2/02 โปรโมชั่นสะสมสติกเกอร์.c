โปรโมชั่นสะสมสติกเกอร์
ห้างสรรพสินค้าแห่งหนึ่งจัดโปรโมชั่นแจกสติกเกอร์ให้ลูกค้าสะสมเพื่อใช้เป็นส่วนลดได้ โดยจำนวนสติกเกอร์ที่สะสมได้จะให้ส่วนลดที่แตกต่างกันไป ตามตารางต่อไปนี้

สะสมครบ 1 ดวง	รับส่วนลด 10%
สะสมครบ 2 ดวง	รับส่วนลด 15%
สะสมครบ 3 ดวง	รับส่วนลด 20%
สะสมครบ 6 ดวง	รับส่วนลด 30%
สะสมครบ 9 ดวง	รับส่วนลด 40%
พิจารณากรณีที่ลูกค้ามีสติกเกอร์ 5 ดวง ลูกค้าจะได้รับส่วนลดเพียง 20% เท่านั้น เนื่องจากสติกเกอร์ไม่เพียงพอที่จะได้ลด 30%

จงเขียนโปรแกรมเพื่อรับจำนวนสติกเกอร์ที่ลูกค้าสะสมได้ (บรรทัดแรก) และราคาสินค้าที่ลูกค้าต้องการซื้อ (บรรทัดที่สอง) แล้วคำนวณส่วนลดที่ลูกค้าได้รับ (บรรทัดที่สาม) จำนวนเงินหลังหักส่วนลดที่ลูกค้าต้องชำระ (บรรทัดที่สี่) และ จำนวนสติกเกอร์คงเหลือ (บรรทัดที่ห้า)

ตัวอย่าง Input/Output 1
5
1000.00 
You get 20 percents discount.
Total amount due is 800.00 Baht.
And you have 2 stickers left.
ตัวอย่าง Input/Output 2
0
1000.0 
You get 0 percents discount.
Total amount due is 1000.00 Baht.
And you have 0 stickers left.
ตัวอย่าง Input/Output 3
20
1000.0 
You get 40 percents discount.
Total amount due is 600.00 Baht.
And you have 11 stickers left.
#include <stdio.h>
#include <stdlib.h>
int main()
{
    char stampin[10], pricein[15];
    int stamp, discount, left;
    float price, total;
    
    fgets (stampin , 10, stdin);
    stamp = atoi(stampin);
    fgets (pricein , 15, stdin);
    price = atof(pricein);
    
    if (stamp >= 9) {
        discount = 40;
        left = stamp - 9;
    } else if (stamp >= 6) {
        discount = 30;
        left = stamp - 6;
    } else if (stamp >= 3) {
        discount = 20;
        left = stamp - 3;
    } else if (stamp >= 2) {
        discount = 15;
        left = stamp - 2;
    } else if (stamp >= 1) {
        discount = 10;
        left = stamp - 1;
    } else {
        discount = 0;
        left = stamp;
    }
    
    total = price - (price * discount / 100);
    printf("You get %d percents discount.\n", discount);
    printf("Total amount due is %.2f Baht.\n", total);
    printf("And you have %d stickers left.", left);
    
    return 0;
}
