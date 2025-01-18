บอกทิศของตำแหน่ง
กำหนดพิกัด x และ y (เป็นข้อมูลชนิด int) ให้นิสิตเขียนโปรแกรมสำหรับตรวจสอบว่าพิกัด (x, y) อยู่ในทิศใด (North, South, East, West, North-east, North-west, South-east, South-west, Center) ดังตัวอย่างด้านล่าง

ตัวอย่างผลลัพธ์ 1
Enter the x coordinate: -5
Enter the y coordinate: 0
West
ตัวอย่างผลลัพธ์ 2
Enter the x coordinate: 0
Enter the y coordinate: 0
Center
ตัวอย่างผลลัพธ์ 3
Enter the x coordinate: -1
Enter the y coordinate: -5
South-west
ตัวอย่างผลลัพธ์ 4
Enter the x coordinate: -1
Enter the y coordinate: 9
North-west
ตัวอย่างผลลัพธ์ 5
Enter the x coordinate: 4
Enter the y coordinate: 5
North-east
ตัวอย่างผลลัพธ์ 6
Enter the x coordinate: 4
Enter the y coordinate: -9
South-east
ตัวอย่างผลลัพธ์ 7
Enter the x coordinate: 0
Enter the y coordinate: 3
North
ตัวอย่างผลลัพธ์ 8
Enter the x coordinate: 3
Enter the y coordinate: 0
East
ตัวอย่างผลลัพธ์ 9
Enter the x coordinate: 0
Enter the y coordinate: -5
South

[hide line #]
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char x_str[5], y_str[5];

    printf("Enter the x coordinate: ");
    fgets(x_str, 5, stdin);
    printf("Enter the y coordinate: ");
    fgets(y_str, 5, stdin);

    int x = atoi(x_str);
    int y = atoi(y_str);
    if(x == 0 && y < 0){
        printf("South");
    }else if (x == 0 && y > 0){
        printf("North");
    }else if (x > 0 && y == 0){
        printf("East");
    }else if (x < 0 && y == 0){
        printf("West");
    }else if (x > 0 && y > 0){
        printf("North-east");
    }else if (x < 0 && y > 0){
        printf("North-west");
    }else if (x < 0 && y < 0){
        printf("South-west");
    }else if (x > 0 && y < 0){
        printf("South-east");
    }else if (x == 0 && y == 0){
        printf("Center");
    }
    return 0;
}