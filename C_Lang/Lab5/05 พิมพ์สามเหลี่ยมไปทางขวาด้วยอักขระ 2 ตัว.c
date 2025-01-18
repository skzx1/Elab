พิมพ์สามเหลี่ยมไปทางขวาด้วยอักขระ 2 ตัว
จงเขียนโปรแกรมเพื่อรับจํานวนเต็มบวกมาหนึ่งจํานวน และพิมพ์สามเหลี่ยมตามขนาดที่ผู้ใช้กําหนดดังตัวอย่างด้านล่าง

ตัวอย่าง Input/Output 1
Enter n: 1
-
ตัวอย่าง Input/Output 2
Enter n: 2
-
-x
- 
ตัวอย่าง Input/Output 3
Enter n: 10
-
-x
-x-
-x-x
-x-x-
-x-x-x
-x-x-x-
-x-x-x-x
-x-x-x-x-
-x-x-x-x-x
-x-x-x-x-
-x-x-x-x
-x-x-x-
-x-x-x
-x-x-
-x-x
-x-
-x
-
ตัวอย่าง Input/Output 4
Enter n: 11
-
-x
-x-
-x-x
-x-x-
-x-x-x
-x-x-x-
-x-x-x-x
-x-x-x-x-
-x-x-x-x-x
-x-x-x-x-x-
-x-x-x-x-x
-x-x-x-x-
-x-x-x-x
-x-x-x-
-x-x-x
-x-x-
-x-x
-x-
-x
-


#include <stdio.h>
#include <stdlib.h>

int main() {
    char nin[100];
    int n;
    printf("Enter n: ");
    fgets(nin, 100, stdin);
    n = atoi(nin);

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (j % 2 == 0){
                printf("-");
            }
            else {
                printf("x");
            }
        }
        printf("\n");
    }
    
    for (int i = n - 1; i > 0; i--) {
        for (int j = 0; j < i; j++) {
            if (j % 2 == 0){
                printf("-");
            }
            else {
                printf("x");
            }
        }
        printf("\n");
    }

    return 0;
}
