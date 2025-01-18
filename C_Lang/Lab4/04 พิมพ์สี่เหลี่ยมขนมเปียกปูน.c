พิมพ์สี่เหลี่ยมขนมเปียกปูน
เขียนโปรแกรมภาษาซี ที่รับเลขจำนวนเต็ม 2 จำนวน เช่น x กับ y (โดย x และ y มีค่าอย่างต่ำเป็น 4) แล้วแสดงสี่เหลี่ยมขนมเปียกปูนที่ยาว x และสูง y ที่มีลักษณะเอียงตามรูป ตัวอย่างเช่น

ตัวอย่างผลลัพธ์ที่ 1
6
4
******
 *    *
  *    *
   ******
ตัวอย่างผลลัพธ์ที่ 2
20
6
********************
 *                  *
  *                  *
   *                  *
    *                  *
     ********************
พิมพ์โปรแกรมของคุณลงในช่องว่างข้างล่างนี้
#include <stdio.h>
#include <stdlib.h>
int main()
{
    char xin[100], yin[100];
    int x, y, i, j;
    fgets(xin, 100 ,stdin);
    x = atoi(xin);
    fgets(yin, 100 ,stdin);
    y = atoi(yin);
    
    if (x < 4 || y < 4) {
        return 0;
    }
    else {
        for(i = 0; i < x; i++)
        {
        printf("*");
        }
        printf("\n");
        
        for (int i = 1; i < y - 1; i++)
        {
             for (int j = 0; j < i; j++) {
                printf(" ");
            }
            printf("*");
            
            for (int j = 0; j < x - 2; j++) {
                printf(" ");
            }
            printf("*\n");
        }
        
        for (int i = 0; i < y - 1; i++)
        {
            printf(" ");
        }
        for (int i = 0; i < x; i++) {
            printf("*");
        }
    }
    return 0;
}