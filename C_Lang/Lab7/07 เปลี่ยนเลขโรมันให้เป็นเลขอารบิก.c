เปลี่ยนเลขโรมันให้เป็นเลขอารบิก
จงเขียนฟังก์ชันเพื่อเปลี่ยนเลขโรมันที่มีค่าอยู่ในช่วงเพียง 1 ถึง 9 (ซึ่งก็คือ I,II,III,IV,V,VI,VII,VIII,IX ตามลำดับ) ทั้งหมดที่ปรากฏในสตริงที่รับผ่านฟังก์ชันเข้ามา ให้กลายเป็นเลขอารบิก 1 หลัก แล้วบันทึกผลที่ได้ลงในตัวแปรอีกตัวที่ถูกส่งเข้ามาด้วยในฟังก์ชัน

ตัวอย่างผลลัพธ์
 Input: There are III eggs on the table.
Output: There are 3 eggs on the table.
 Input: II + III = V
Output: 2 + 3 = 5

[hide line #]
#include <stdio.h>

[hide line #]
void roman2arabic(char input[],char output[])
{
    int i = 0, j = 0;
    while (input[i] != '\0') {
        if (input[i] == 'I') {
            switch (input[i + 1]) {
                case 'I':
                    if (input[i + 2] == 'I') { 
                        output[j++] = '3';
                        i += 3;
                    } else {
                        output[j++] = '2';
                        i += 2;
                    }
                    break;
                case 'V':
                    output[j++] = '4';
                    i += 2;
                    break;
                case 'X':
                    output[j++] = '9';
                    i += 2;
                    break;
                default:
                    output[j++] = '1';
                    i++;
                    break;
            }
        } else if (input[i] == 'V') {
            switch (input[i + 1]) {
                case 'I':
                    if (input[i + 2] == 'I') {
                        if (input[i + 3] == 'I') {
                            output[j++] = '8'; 
                            i += 4;
                        } else {
                            output[j++] = '7';
                            i += 3;
                        }
                    } else {
                        output[j++] = '6';
                        i += 2;
                    }
                    break;
                default:
                    output[j++] = '5';
                    i++;
                    break;
            }
        } else if (input[i] == 'X') {
            output[j++] = 'X';
            i++;

            int count = 0;
            while (input[i] == 'I') {
                count++;
                i++;
            }
            if (count > 0) {
                output[j++] = '0' + count;
            }
        } else {
            output[j++] = input[i++];
        }
    }

    output[j] = '\0';
    }

int main()
{  char input[80],output[80];

   printf(" Input: ");
   fgets(input, 80, stdin);
   char *ch = input;
   while (*ch++ != '\n' || (*(--ch) = 0));

   roman2arabic(input,output);
   printf("Output: %s\n",output);

   return 0;
}