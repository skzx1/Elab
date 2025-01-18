The Value of \( \pi \)
Calculate the value of \( \pi \) from the infinite series

\[ \pi = 4 - \frac{4}{3} + \frac{4}{5} - \frac{4}{7} + \frac{4}{9} - \frac{4}{11} + ... \]

Write the program to input integer n where n > 0

and print the value of \( \pi \) approximated by n term of this series

Example 1
Enter n: 3
3.4666666667
Example 1
Enter n: 100000
3.1415826536

#include <stdio.h>
int main()
{
    int n, i;
    double pi = 0;
    
    printf("Enter n: ");
    scanf("%d", &n);
    if (n < 0){
        return 0;
    }
    
    for(i = 0; i < n; i++){
        if (i % 2 == 0){
            pi += 4.0 / (2 * i + 1);
        }
        else{
            pi -= 4.0 / (2 * i + 1);
        }
    }
    printf("%.10f", pi);
    return 0;
}