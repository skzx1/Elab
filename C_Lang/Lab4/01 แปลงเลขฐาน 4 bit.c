แปลงเลขฐานสิบเป็นเลขฐานสอง (ขนาด 4 บิต)
ให้นิสิตเขียนโปรแกรมรับเลขจำนวนเต็มฐานสิบซึ่งมีค่าตั้งแต่ 0 ถึง 15 และแปลงค่าเป็นเลขฐานสองขนาด 4 บิต แล้วพิมพ์ออกมา

ให้นิสิตเขียนโปรแกรมโดยใช้ bitwise operator และไม่ใช้ if statement

ตัวอย่างข้อมูลส่งออก
7
Binary number of 7 is 0111.


#include <stdio.h>
#include <stdlib.h>
int main() {
    char numin[5];
    int n, bit0, bit1, bit2, bit3;
    fgets(numin, 5, stdin);
    n = atoi(numin);
    bit0 = n & 1;
    bit1 = n >> 1 & 1;
    bit2 = n >> 2 & 1;
    bit3 = n >> 3 & 1;
    printf("Binary number of %d is %d%d%d%d.",n, bit3, bit2, bit1, bit0);
    return 0;
}