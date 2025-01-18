Shift Array
จงเขียนฟังก์ชัน shift_left(char str[], int n); ที่มีหน้าที่เลื่อนตัวอักษรใน array ของตัวอักษร (str) ไปทางซ้ายตามจำนวนครั้งที่กำหนด (n) หากเลื่อนไปจนสุด array แล้วตัวอักษรที่หลุดออกจากซ้ายสุดจะถูกนำกลับมาต่อที่ด้านขวาสุด (ลักษณะการหมุนแบบวงกลม)

กำหนดให้ฟังก์ชันมีพารามิเตอร์ 2 ตัว คือ char str[] และ int n โดย

str คือ array ของตัวอักษรที่ต้องการเลื่อนตำแหน่ง
n คือ จำนวนเต็มบวก หรือศูนย์ แทนจำนวนครั้งที่ต้องการเลื่อนตัวอักษรไปทางซ้าย
ห้ามสร้าง array ใหม่เพื่อจัดเก็บผลลัพธ์ (ต้องแก้ไขใน array เดิมเท่านั้น)

ตัวอย่างผลลัพธ์ จาก main function ที่กำหนดให้
String: Computer Programming
     n: 4
Output: >>uter ProgrammingComp<<


[hide line #]

#include <stdio.h>
#include <stdlib.h>

void shift_left(char str[], int n);

int main()
{  char str[80], *c;
   int n;

   printf("String: ");
   fgets(str, sizeof(str), stdin);
   for (c=str; *c && *c != '\n'; c++)
       ;
   *c = 0;
   printf("     n: ");
   scanf("%d", &n);
   shift_left(str, n);
   printf("Output: >>%s<<\n",str);
   return 0;
}

// ส่งเฉพาะ implementation ของฟังก์ชัน shift_left
void shift_left(char str[], int n) {
    int i, j, len = 0;
    char temp;
     while (str[len] != '\0' && str[len] != '\n') {
        len++;
     }
      if (len == 0) {
        return;
    }
    
    n = n % len;
    
    for (i = 0; i < n; i++) {
        temp = str[0];
        for (j = 0; str[j] != '\0'; j++) {
            str[j] = str[j + 1];
        }
        str[j - 1] = temp;
    }
}