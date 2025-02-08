ซ่คำ (Word Chain)
โซ่คำ คือลำดับของคำที่มีจำนวนอักขระเท่ากันและแต่ละคำที่มีลำดับติดกันจะต้องมีตำแหน่งที่มีตัวอักขระต่างกันไม่เกินสองตำแหน่ง เช่น HEAD และ HEAP จะต่างกันตำแหน่งเดียวคือ D และ P ในตำแหน่งตัวอักขระที่ 4 ของคำ ในขณะที่ REAR กับ BAER จะมีตำแหน่งต่างกัน 3 ตำแหน่ง คือ ตำแหน่งที่ 1 (R กับ B) ตำแหน่งที่ 2 (E และ A) และ ตำแหน่งที่ 3 (A และ E)

ตัวอย่างของโซ่คำที่ต่อเนื่องได้แก่ HEAD HEAP LEAP TEAR REAR และ EGG EAG GAE GAP TAP TIN

ตัวอย่างของโซ่คำที่ขาดได้แก่ LEAP TEAR REAR BAER BAET BEEP ซึ่งจะขาดที่ คำว่า BAER

Task
ให้เขียนโปรแกรมที่รับชุดของโซ่คำเข้ามาชุดหนึ่ง แล้วหาคำสุดท้ายในโซ่คำ ก่อนที่โซ่คำจะขาด

Input
บรรทัดแรก เก็บจำนวนเต็ม L แทนจำนวนตัวอักษรของแต่ละคำ โดยที่ 3 <= L < 1000

บรรทัดที่สอง เก็บจำนวนเต็ม N แทนจำนวนคำทั้งหมดในแฟ้มข้อมูล โดยที่ 1 < N < 30000

บรรทัดที่ 3..(N + 2) เก็บลำดับของคำที่มีจำนวนตัวอักขระ L ตัว แต่ละบรรทัดเก็บคำที่เขียนด้วยตัวอักษร (‘A’ ถึง ‘Z’ ) ที่เป็นตัวพิมพ์ใหญ่

Output
ผลลัพธ์ มี 1 บรรทัด แสดงคำสุดท้ายของโซ่คำชุดแรก



Example with comment
Input

4
12
HEAD         <--------- คำเริ่มต้น
HEAP         <--------- ผิด 1 ตัวอักษร 
LEAP
TEAR
REAL         <--------- ผิด 2 ตัวอักษร 
BAER         <--------- ผิด 4 ตัวอักษร (ตัด Chain ที่คำว่า REAL) 
BAET
BEEP
JEEP
JOIP
JEIP
AEIO
Output
REAL
Example1
4
12
HEAD
HEAP
LEAP
TEAR
REAR
BAER 
BAET
BEEP
JEEP
JOIP
JEIP
AEIO
Output
REAR
Example2
7
10
OAKVALE
OAKVELA
BAABABB
AAVAELA
AAAAELA
AAAAALA
AAAAAAA
AAAAABB
AAAABBA
BAABABB
Output

OAKVELA


#include <stdio.h>

int wordchain(int len, char *word1, char *word2) {
    int count = 0, i;
    for (i = 0; i < len; i++) {
        if (word1[i] != word2[i]) {
            count++;
        }
        if (count > 2) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int l, n, i;
    scanf("%d", &l);
    scanf("%d", &n);

    char words[n][l + 1];
    for (i = 0; i < n; i++) {
        scanf("%s", words[i]);
    }

    char *lword = words[0];
    for (i = 1; i < n; i++) {
        if (wordchain(l, lword, words[i])) {
            lword = words[i]; 
        } else {
            printf("%s\n", lword);
            return 0;
        }
    }

    printf("%s\n", lword);
    return 0;
}
