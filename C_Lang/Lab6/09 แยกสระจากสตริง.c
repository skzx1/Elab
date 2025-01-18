แยกสระจากสตริง
จงเขียนฟังก์ชัน str_extract(char** source, char** vowel); ที่แยกอักขระที่เป็นสระออกจาก source ไปเก็บไว้ที่ vowel

โดยพิจารณาโค้ดของฟังก์ชัน main ที่กำหนดให้ต่อไปนี้

ตัวอย่างข้อมูลเข้า/ข้อมูลออก เมื่อ main function ทำงานถูกต้อง
ตัวอย่างที่ 1
Hello World
Consonants: "Hll Wrld"
    Vowels: "eoo"
ตัวอย่างที่ 2
Computer Programming
Consonants: "Cmptr Prgrmmng"
    Vowels: "oueoai"
ห้ามใช้ library นอกเหนือจากที่กำหนดให้


[hide line #]
#include <stdio.h>
#include <stdlib.h>

void str_extract(char** source, char** vowel);

int main() {
    char* str = malloc(201);
    scanf("%[^\n]s", str);
    char* vowel = NULL;

    str_extract(&str, &vowel);

    printf("Consonants: \"%s\"\n", str);
    printf("    Vowels: \"%s\"\n", vowel);

    free(str);
    free(vowel);
    return 0;
}
ส่งเฉพาะ implementation ของ str_extract(char** source, char** vowel);
#include <stdio.h>
#include <stdlib.h>

void str_extract(char** source, char** vowel) {
    char* vowels = malloc(201);
    int i;
    int voi = 0, coi = 0;
    char* consonants = *source;

    for (i = 0; (*source)[i] != '\0'; i++) {
        char alp = (*source)[i];
        if (alp == 'a' || alp == 'e' || alp == 'i' || alp == 'o' || alp == 'u' ||
            alp == 'A' || alp == 'E' || alp == 'I' || alp == 'O' || alp == 'U') {
            vowels[voi++] = alp;
        } else {
            consonants[coi++] = alp;
        }
    }

    vowels[voi] = '\0';
    consonants[coi] = '\0';
    *vowel = vowels;
}