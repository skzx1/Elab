ต้องการสร้าง array a ดังตัวอย่างด้านล่าง จงเติมโค้ดให้สมบูรณ์

Sample Output 1
Enter the number of rows or columns: 3
 1  2  3 
 2  3  4 
 3  4  5 
Sample Output 2
Enter the number of rows or columns: 10
 1  2  3  4  5  6  7  8  9 10
 2  3  4  5  6  7  8  9 10 11 
 3  4  5  6  7  8  9 10 11 12 
 4  5  6  7  8  9 10 11 12 13 
 5  6  7  8  9 10 11 12 13 14
 6  7  8  9 10 11 12 13 14 15
 7  8  9 10 11 12 13 14 15 16
 8  9 10 11 12 13 14 15 16 17
 9 10 11 12 13 14 15 16 17 18
10 11 12 13 14 15 16 17 18 19  

[hide line #]
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, j;
    printf("Enter the number of rows or columns: ");
    scanf("%d",&n);
    int **a =
(int**)malloc(n * sizeof(int*))
;
    for(
i = 0; i < n; i++
) {
        a[i] =
(int*)malloc(n * sizeof(int))
;
    }

    // Assign value to array a
    
for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++)
           a[i][j] = i + j + 1;
    }


    // Print all values in array a
    for(
i = 0; i < n; i++
 ) {
        for(
j = 0; j < n; j++
)
            printf("
%2d 
", a
[i][j]
);
        printf("\n");
    }
    return 0;
}