ภาพวาดรูปแบบหนึ่งที่มักเห็นประจำในอินเดียก็คือ ภาพวาดที่เรียกว่า รังโกลี (Rangoli) ซึ่งเป็นรูปแบบหนึ่งของศิลปะที่นิยมมากที่สุดในอินเดียก็ว่าได้ เป็นการวาดภาพด้วยทรายหรือผงสี บนพื้นขาวหรือพื้นสี ซึ่งมักใช้ตกแต่งหน้าบ้านของชาวอินเดียในงานเทศกาลต่างๆ หรือในสถานที่จัดงานสำคัญๆ หมายถึงการต้อนรับขับสู้อย่างอบอุ่นของเจ้าบ้านหรือเจ้าภาพต่อแขกที่มาเยือน

ในข้อนี้จะให้เขียนโปรแกรมเพื่อวาดภาพรังโกลี จากตัวอักษรภาษาอังกฤษ โดยรับข้อมูลเป็นจำนวนเต็มบวก N (N <= 26) ซึ่งเป็นขนาดของภาพรังโกลี และเป็นลำดับอักษรภาษาอังกฤษสูงสุดที่ใช้ในภาพ เช่น N = 3 หมายถึงใช้ตัวอักษรภาษาอังกฤษ a, b และ c เท่านั้น

ขนาดของภาพรังโกลีมีลักษณะดังนี้

#Size N = 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#Size N = 10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------

จากภาพรังโกลีขนาด 10 จะเห็นว่า ตัวอักษรที่ใช้วาดตัวนอกสุดคือ j ซึ่งเป็นตัวอักษรตัวที่ 10 ในภาษาอังกฤษ ถัดมาข้างในเป็น i, h, g, f, e, d, c, b, และ a ตามลำดับ

หมายเหตุ

หากสร้างภาพรังโกลีไม่ได้ ให้พิมพ์ -
ตัวอย่างโปรแกรม 1

10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
ตัวอย่างโปรแกรม 2

0
-

#include <stdio.h>
#include <stdlib.h>
int main() {
    char numin[100], alp;
    int n, i, j;
    int alptop, alpbot;

    fgets(numin, 100, stdin);
    n = atoi(numin);

    if(n == 0 || n < 1 || n > 26 ){
    printf("-");
    return 0;
    }
    else{
        //ส่วนบน
        for (i = 0; i < n; i++) {
            alptop  = 2 * (n - i - 1);
    
            for (j = 0; j < alptop; j++) {
                printf("-");
            }
            for (j = 0; j < i + 1; j++) {
                alp = 'a' + (n - 1 - j);
                printf("%c", alp);
                if (j != i) {
                    printf("-");
                }
            }
            for (j = i - 1; j >= 0; j--) {
                alp = 'a' + (n - 1 - j);
                printf("-");
                printf("%c", alp);
            }
            for (j = 0; j < alptop; j++) {
                printf("-");
            }
            printf("\n");
        }
        
        //ส่วนล่าง
        for (i = n - 2; i >= 0; i--) {
            alpbot = 2 * (n - i - 1);
    
            for (j = 0; j < alpbot; j++) {
                printf("-");
            }
            for (j = 0; j < i + 1; j++) {
                alp = 'a' + (n - 1 - j);
                printf("%c", alp);
                if (j != i) {
                    printf("-");
                }
            }
             for (j = i - 1; j >= 0; j--) {
                alp = 'a' + (n - 1 - j);
                printf("-");
                printf("%c", alp);
            }
            for (j = 0; j < alpbot; j++) {
                printf("-");
            }
            printf("\n");
        }
    }
    return 0;
}