ลบสระออกจากสายอักขระ
จงเขียนฟังก์ชันเพื่อลบสระที่ปรากฏในสายอักขระที่ส่งผ่านฟังก์ชันเข้ามาออกให้หมด

ตัวอย่างผลลัพธ์ 1
 Input: hello, world
Output: hll, wrld
ตัวอย่างผลลัพธ์ 2
 Input: abcdef 123456
Output: bcdf 123456

#include <stdio.h>

int remove_vowel(
char *str
)
{
int i = 0, j = 0;
int count = 0;

    for (i = 0; str[i] != '\0' && str[i] != '\n'; i++) {
        char alp = str[i];
        if (alp == 'a' || alp == 'e' || alp == 'i' || alp == 'o' || alp == 'u' ||
            alp == 'A' || alp == 'E' || alp == 'I' || alp == 'O' || alp == 'U') 
            {
            count++;
            } 
            else {
                str[j++] = alp;
        }
    }

    str[j] = '\0';
    return count;

}

int main()
{  char str[80];

  printf(" Input: ");
  fgets(str, 80, stdin);

  remove_vowel(str);
  printf("Output: %s\n",str);

  return 0;
}
