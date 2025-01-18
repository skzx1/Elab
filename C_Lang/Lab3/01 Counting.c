Write a program that get an integer n and print the number from n down to 0 if n >= 0

Example 1
13
13
12
11
10
9
8
7
6
5
4
3
2
1
0
Example 2
0
0
Example 3
-1
Example 4
1
1
0
Complete the program below


#include <stdio.h>
#include <stdlib.h>
int main(){
    char input[5];
    int num;
    fgets (input, 5, stdin);
    num = atoi(input);
    if (num < 0){
        return 0;
    }
    else{
        while(num >= 0){
            printf("%d\n", num);
            num--;
        }
    }

return 0;
}
