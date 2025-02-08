Combine 2 arrays
Write a program which takes 2 arrays of 5 integers each, a[] and b[]. c[] is an array with 10 integers. The program should put into c[] the appending of b[] to a[], the first 5 integers of c[] from array a[], the latter 5 from b[]. Then the program should display c[].

ตัวอย่างผลลัพธ์
Enter array a: 
Please enter an integer: 1
Please enter an integer: 2
Please enter an integer: 3
Please enter an integer: 4
Please enter an integer: 5
Enter array b:
Please enter an integer: 20
Please enter an integer: 21
Please enter an integer: 22
Please enter an integer: 23
Please enter an integer: 24
Array c: 1 2 3 4 5 20 21 22 23 24 


#include <stdio.h>

int main()
{
  int i, a[5],b[5],c[10] ;
printf("Enter array a: \n");
    for (i=0;i<5;i++){
        printf("Please enter an integer: ");

    scanf ("%d",&a[i]);
}
printf("Enter array b: \n");
    for (i=0;i<5;i++){
        printf("Please enter an integer: ");

    scanf ("%d",&b[i]);
}
 for (i = 0; i < 5; i++){
        c[i] = a[i];
        c[i + 5] = b[i];
    }

  printf ("Array c: ");
  for (i=0;i<10;i++)
    printf ("%d ",c[i]);

  printf ("\n");
  return 0;
}