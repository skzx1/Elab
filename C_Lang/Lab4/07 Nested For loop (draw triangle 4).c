Draw triangle 4 #
Your job is to write a program to draw a triangle.

The program receives a number n as a height of triangle.

Then the program print a triangle with the height = n and base = (2n-1) using *, with the base on the left of the screen, as in the examples.

Sample output 1

2
*
**
*
Sample output 2

9
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
#include <stdio.h>
#include <stdlib.h>

int main() {
    char xin[100];
    int x;

    fgets(xin, 100, stdin);
    x = atoi(xin);

    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
    for (int i = x - 1; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
