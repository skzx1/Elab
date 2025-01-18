ให้เขียนโปรแกรมจำลองการไต่ขั้นบันได โดยเริ่มแรก โปรแกรมจะถามจำนวนขั้นบันได (บรรทัดที 1)
จากนั้น ในแต่ละรอบ โปรแกรมจะแสดงตำแหน่งปัจจุบันของคนบนขั้นบันได และโปรแกรมจะถาม step command

step command สำหรับโปรแกรมนี้ คือ

ถ้าเป็นจำนวนเต็มบวก x หมายถึง ให้ไต่บันไดขึ้นไป x ขั้น
ถ้าเป็นจำนวนเต็มลบ -x หมายถึง ให้ไต่บันไดลงมา x ขั้น
ถ้าเป็นจำนวนเต็มศูนย์ หมายถึง จบโปรแกรม
เงื่อนไขเพิ่มเติมของโปรแกรมนี้ คือ

คน ประกอบด้วย 2 ส่วน คือ ส่วนหัว (O) และส่วนขา (^)
รอบที่หนึ่ง ขาของคนจะอยู่ที่ขั้นบันไดล่างสุด
ขาของคนจะไม่อยู่ต่ำกว่าบันไดขั้นล่างสุด และหัวของคนจะไม่อยู่สูงกว่าบันไดขั้นบนสุด
Sample Output 1
Input number of stairs: 4
---- round 1 ----
|---|
|---|
|-O-|
|-^-|
Input step command: 1
---- round 2 ----
|---|
|-O-|
|-^-|
|---|
Input step command: 0
Sample Output 2
Input number of stairs: 4
---- round 1 ----
|---|
|---|
|-O-|
|-^-|
Input step command: 2
---- round 2 ----
|-O-|
|-^-|
|---|
|---|
Input step command: 2
---- round 3 ----
|-O-|
|-^-|
|---|
|---|
Input step command: 0
Sample Output 3
Input number of stairs: 4
---- round 1 ----
|---|
|---|
|-O-|
|-∧-|
Input step command: 2
---- round 2 ----
|-O-|
|-∧-|
|---|
|---|
Input step command: -1
---- round 3 ----
|---|
|-O-|
|-∧-|
|---|
Input step command: -2
---- round 4 ----
|---|
|---|
|-O-|
|-∧-|
Input step command: -1
---- round 5 ----
|---|
|---|
|-O-|
|-∧-|
Input step command: 0



#include <stdio.h>
int main() {
    int n, i, step, count = 0, r = 1;

    printf("Input number of stairs: ");
    scanf("%d", &n);
    printf("---- round %d ----\n", r);
    r++;
    
    for (i = 0; i < n; i++) {
        if (i == n - 2) {
            printf("|-O-|\n");
        } else if (i == n - 1) {
            printf("|-^-|\n");
        } else {
            printf("|---|\n");
        }
    }

    while (n != 0) {
        printf("Input step command: ");
        scanf("%d", &step);

        if (step == 0) {
            return 0;
        }
        count += step;

        if (count < 0) {
            count = 0;
        } else if (count > n - 2) {
            count = n - 2;
        }

        printf("---- round %d ----\n", r);
        r++;

        for (i = 0; i < n; i++) {
            if (i == n - 2 - count) {
                printf("|-O-|\n");
            } else if (i == n - 1 - count) {
                printf("|-^-|\n");
            } else {
                printf("|---|\n");
            }
        }
    }

    return 0;
}
