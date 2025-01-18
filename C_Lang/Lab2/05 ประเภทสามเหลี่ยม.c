จงเขียนโปรแกรมเพื่อรับขนาดของด้าน 3 ด้านของสามเหลี่ยมเป็นจำนวนเต็ม แล้วให้คำตอบว่า 3 ด้านที่ให้นั้นเป็นสามเหลี่ยมประเภทใด โดยสามเหลี่ยมแต่ละประเภทมีลักษณะดังต่อไปนี้

ไม่ใช่สามเหลี่ยม (invalid) เกิดขึ้นเมื่อ
ผลรวมของ 2 ด้านน้อยกว่าหรือเท่ากับอีกด้านที่เหลือ
มีด้านอย่างน้อย 1 ด้านที่น้อยกว่าหรือเท่ากับ 0
สามเหลี่ยมด้านเท่า (equilateral) ทั้งสามด้านเท่ากัน
สามเหลี่ยมหน้าจั่ว (isosceles) เท่ากันแค่ 2 ด้าน
สามเหลี่ยมด้านไม่เท่า (scalene) ไม่มีด้านใดเท่ากัน
ตัวอย่าง Input/Output 1
Enter length of side A: 3
Enter length of side B: 3
Enter length of side C: 3
Triangle type is equilateral.
ตัวอย่าง Input/Output 2
Enter length of side A: 3
Enter length of side B: 2
Enter length of side C: 2
Triangle type is isosceles.
ตัวอย่าง Input/Output 3
Enter length of side A: 3
Enter length of side B: 4
Enter length of side C: 5
Triangle type is scalene.
ตัวอย่าง Input/Output 4
Enter length of side A: 4
Enter length of side B: 2
Enter length of side C: 2
Triangle type is invalid.

[hide line #]
#include <stdio.h>
#include <stdlib.h>
int main(){
char ain[4] , bin[4], cin[4];
int a, b, c;
printf("Enter length of side A: ");
fgets(ain, 4, stdin);
a = atoi(ain);

printf("Enter length of side B: ");
fgets(bin, 4, stdin);
b = atoi(bin);

printf("Enter length of side C: ");
fgets(cin, 4, stdin);
c = atoi(cin);

if (a <= 0 || b <= 0 || c <= 0 || a + b <= c || a + c <= b || b + c <= a) {
    printf("Triangle type is invalid.");
} else if (a == b && b == c) {
    printf("Triangle type is equilateral.");
} else if (a == b || b == c || a == c) {
    printf("Triangle type is isosceles.");
} else if (a != b && b != c && a != c){
    printf("Triangle type is scalene.");
}
return 0;
}