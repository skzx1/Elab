    นับสระในสายอักขระ
เขียนโปรแกรมภาษาซี รับ string เข้ามาหนึ่ง string ด้วย scanf() แล้วแสดงสระที่มีทั้งหมดใน string ดังกล่าวออกมา พร้อมกับแสดงจำนวนตัวอักขระที่เป็นสระด้วย ดังตัวอย่าง

ตัวอย่างผลลัพธ์ที่ 1
String (without a space): hello
e o 
This string contains 2 vowels.
ตัวอย่างผลลัพธ์ที่ 2
String (without a space): string
i 
This string contains 1 vowel.
ตัวอย่างผลลัพธ์ที่ 3
String (without a space): zzzZZ!

This string contains 0 vowel.

#include <stdio.h>

int main() {
char word[100];
    int count = 0, i;
    
    printf("String (without a space): ");
    scanf("%s", word);

    for (i = 0; word[i] != '\0'; i++) {
        char alp = word[i];
        if (alp == 'a' || alp == 'e' || alp == 'i' || alp == 'o' || alp == 'u' ||
            alp == 'A' || alp == 'E' || alp == 'I' || alp == 'O' || alp == 'U') 
            {
            printf("%c ", alp);
            count++;
        }
    }
    if (count <= 1){
        printf("\nThis string contains %d vowel.", count);
    }
    else{
        printf("\nThis string contains %d vowels.", count);
    }

}