คอมพิวเตอร์ทำงาน
จงเขียนโปรแกรมเพื่อแสดงผลเวลาที่เครื่องคอมพิวเตอร์ทำงานในรูปของจำนวนวัน ชั่วโมง และนาที ตามลำดับ (ไม่ต้องคำนึงถึงการรับข้อมูลเข้า)

เมื่อตัวแปร computer_time เก็บค่าจำนวนนาทีที่เครื่องคอมพิวเตอร์ทำงาน

ตัวอย่างผลลัพธ์เมื่อ computer_time มีค่า 785
It is 0 days 13 hours and 5 minutes.
อธิบาย: คอมพิวเตอร์ทำงาน 785 นาที เท่ากับ 0 วัน 13 ชั่วโมง 5 นาที

ตัวอย่างผลลัพธ์เมื่อ computer_time มีค่า 1678
It is 1 days 3 hours and 58 minutes.
อธิบาย: คอมพิวเตอร์ทำงาน 1678 นาที เท่ากับ 1 วัน 3 ชั่วโมง 58 นาที

#include<stdio.h>
int main() {
    int computer_time = 785;  // ในโปรแกรมตรวจอาจเปลี่ยนค่าของตัวแปรนี้ แต่นิสิตไม่ต้องเปลี่ยนค่าของตัวแปรนี้
    int days, hours, minutes;
    int c;
    days = computer_time / 1440;
    computer_time -= days * 1440;
    hours = computer_time / 60;
    computer_time -= hours * 60;
    minutes = computer_time % 60;

    printf("It is %d days %d hours and %d minutes.", days, hours, minutes);
     return 0;
}