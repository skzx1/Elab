Automorphic numbers

Automorphic numbers คือตัวเลขใด ๆ ที่เมื่อนำมายกกำลังสองแล้วยังคงได้ตัวเลขที่ลงท้ายด้วยตัวเลขที่เอามายกกำลัง

ตัวอย่างเช่น
1
2
=
1

5
2
=
25

6
2
=
36

25
2
=
625

76
2
=
5776

จากตัวอย่างข้างต้นจะได้ว่า 1, 5, 6, 25 และ 76 ต่างก็เป็น Automorphic numbers

จงเขียนโปรแกรมที่รับค่า input เป็นเลขจำนวนเต็มบวกใด ๆ โดยโปรแกรมจะทำการตรวจสอบว่าตัวเลขดังกว่าเป็น Automorphic numbers หรือไม่ดังตัวอย่าง

หมายเหตุ input ในชุดทดสอบ มีค่าไม่เกิน 100,000,000

sample output
Input n = 25
n^2 = 625
Yes. 25 is automorphic number.
sample output2
Input n = 13
n^2 = 169
No. 13 is not automorphic number.
โปรแกรมที่เขียนได้คือ
#include <stdio.h>
int main()
{   
    long long n, dn, oldn;
    printf("Input n = ");
    scanf("%lld", &n);
    if (n < 0 || n > 100000000) {
        return 1;
    }
    oldn = n;
    dn = n * n;

    printf("n^2 = %lld", dn);

    while (n > 0){
        if(n % 10 != dn % 10){
            printf("\nNo. %lld is not automorphic number.", oldn);
            return 0;
        }
    n /= 10;
    dn /= 10;
    }
    printf("\nYes. %lld is automorphic number.", oldn);
    return 0;
}