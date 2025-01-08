จงเขียนโปรแกรมเพื่อคำนวณค่าปริมาตร (volume) ของทรงกลม ในรูปแบบทศนิยม 2 ตำแหน่ง โดยค่ารัศมี (ตัวแปร radius) เป็นจำนวนจริง

โดยใช้การคำนวณจากสูตร \[ volume = \frac{4}{3}\times\pi\times radius^3 \] กำหนดค่าคงที่ \(\pi=\frac{22}{7}\)

ตัวอย่างผลลัพธ์ เมื่อตัวแปร radius มีค่า 1.5

The volume of this sphere is 14.14
#include <stdio.h>
#include <stdlib.h>

// กำหนดค่าคงที่ PI มีค่า 22.0/7
#define PI 22.0/7

int main()
{
    float radius = 1.5;
    float volume;
float asw;
volume = PI * radius * radius * radius ;
asw = volume * 4/3;
printf("The volume of this sphere is %.2f", asw);
    return 0;
}