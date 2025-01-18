ให้เขียนโปรแกรมสำหรับตรวจสอบว่าตัวอักษรที่พิมพ์เข้ามาเป็นอักษรชนิด ตัวพิมพ์เล็ก (lower case), ตัวพิมพ์ใหญ่ (upper case), ตัวเลข (digit), หรือเป็นอักษรประเภทอื่น (others)

ตัวอย่างผลลัพธ์
b
Output: lower case 
7
Output: digit
W
Output: upper case
+
Output: others
#include <stdio.h>
int main()
{
    char input[5];
    fgets(input, 5, stdin);
    if (input[0] >= 'a' && input[0] <= 'z'){
        printf("Output: lower case");
    }else if (input[0] >= 'A' && input[0] <= 'Z'){
        printf("Output: upper case");
    }else if (input[0] >= '0' && input[0] <= '9'){
        printf("Output: digit");
    }else{
        printf("Output: others");
    }

    return 0;
}