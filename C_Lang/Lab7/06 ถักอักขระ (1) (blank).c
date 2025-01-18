ถักอักขระ (1)
จงเติมโค้ดเพื่อให้โปรแกรมสามารถทำงานได้อย่างสมบูรณ์ โดยที่ฟังก์ชัน int charcount(char *s) จะนับจำนวนอักขระที่ปรากฏอยู่ในสายอักษรที่ส่งผ่านเข้ามาในฟังก์ชันตั้งแต่อักขระตัวแรกจนถึงอักขระตัวสุดท้ายก่อนหน้าอักขระนัลล์ (null character)

ส่วนฟังก์ชัน void charweave(char *s,char *result) จะถักอักขระโดยเก็บผลลัพธ์ของการถักนี้ไว้ในตัวแปร result การถักอักขระมีลักษณะดังนี้ สมมติให้ตัวแปร s มีอักขระอยู่ n ตัวและรูปแบบการเรียงของอักขระเป็น C1C2C3C4...Cn ดังนั้นผลลัพธ์ที่ได้จากถักจะมีลักษณะเป็น C1CnC2Cn-1C3Cn-2C4Cn-3...Cn-1C2CnC1

ตัวอย่างผลลัพธ์
String: hello, world
Output: hdellrloow,  ,woolrlledh
String: 12345
Output: 1524334251

[hide line #]
#include <stdio.h>
#include <stdlib.h>

int charcount(char *s)
{
   
int count;
   for(count = 0; s[count] != '\0'; count++);
   return count;

}

void charweave(char *s,char *result)
{
int len = charcount(s);
int i = 0 ,ri = 0, j = 0;
int revlen = len;

  while (i < len / 2) {
    result[j++] = s[i++];

    result[j++] = s[--revlen];
  }
  if (len % 2 == 1) {
    result[j++] = s[i];

    result[j++] = s[i];
  }
  
  ri = len / 2;
  
  while (ri > 0) {
    result[j++] = s[revlen++];

    result[j++] = s[--ri];
  }
result[j] = '\0';

}

int main()
{  char str[100],result[200];

   printf("String: ");
   fgets(str, 100, stdin);
   char *ch = str;
   while (*ch++ != '\n' || (*(--ch) = 0));
   charweave(str,result);
   printf("Output: %s\n",result);
   return 0;
}