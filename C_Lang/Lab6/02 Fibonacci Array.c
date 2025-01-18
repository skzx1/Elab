Fibonacci Array
ให้เขียนฟังก์ชัน unsigned long *fibo_array(unsigned int n, double *golden_ratio); ที่คืนค่า array ของเลขฟิโบนัชชีจำนวน n ตัวแรก และคำนวณอัตราส่วนทองคำของเลขฟิโบนัชชีใน array เก็บไว้ที่ pointer golden_ratio

เลขฟิโบนัชชี หาได้จาก ผลรวมของตัวเลข 2 ตัวก่อนหน้า หรือ F[i] = F[i - 1] + F[i - 2] เมื่อ F[0] = 0 และ F[1] = 1

อัตราส่วนทองคำ หาได้จาก อัตราส่วนของเลขฟิโบนัชชีลำดับที่ n + 1 ต่อเลขฟิโบนัชชีลำดับที่ n

ตัวอย่าง array ของเลขฟิโบนัชชี 10 ตัวแรก คือ {0, 1, 1, 2, 3, 5, 8, 13, 21, 34} ซึ่งมีอัตราส่วนทองคำ คือ F[11] / F[10] = 89 / 55


[hide line #]
#include <stdio.h>
#include <stdlib.h>

unsigned long *fibo_array(unsigned int n, double *golden_ratio);

int main() {
    // เขียนฟังก์ชัน main เพื่อทดสอบฟังก์ชัน fibo_array เอง
    return 0;
}

// ส่งเฉพาะ implementation ของฟังก์ชัน unsigned long *fibo_array(unsigned int n, double *golden_ratio);
unsigned long *fibo_array(unsigned int n, double *golden_ratio){
    unsigned long *fibonacci = (unsigned long *)malloc(n * sizeof(unsigned long));
    fibonacci[0] = 0;
    fibonacci[1] = 1;
    for (int i = 2; i < n; i++){
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    }
    *golden_ratio = ((double)fibonacci[n - 1] + fibonacci[n - 1] + fibonacci[n - 2]) / ((double)fibonacci[n - 2] + fibonacci[n - 1]);
    return fibonacci;
}