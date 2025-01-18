แปลงเลขฐาน (recursion)
ให้เขียนโปรแกรม เพื่อแปลงเลขฐานสิบ เป็นเลขฐานสอง โดยใช้ Recursion

ตัวอย่าง
10
1010
123
1111011
#include <stdio.h>
#include <stdlib.h>
int dectobin(int n) {
    int bin;
    if (n == 0) {
        return 0;
    }
    dectobin(n >> 1);
    bin = n & 1;
    printf("%d", bin);
}

int main()
{
    char numin[50];
    int dec;
    
    fgets(numin, 50, stdin);
    dec = atoi(numin);

    if (dec == 0) {
        printf("0");
    }
    else {
        dectobin(dec);
    }
    return 0;
}