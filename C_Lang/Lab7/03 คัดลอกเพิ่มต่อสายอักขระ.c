จงเขียนฟังก์ชัน stringcat เพื่อคัดลอกสายอักขระที่เก็บอยู่ในตัวแปร src ไปเพิ่มต่อท้ายข้อมูลที่มีอยู่ในตัวแปร dest

ตัวอย่างผลลัพธ์
Input 1: hello
Input 2: world
 Output: worldhello
Input 1: 12345 67890
Input 2: abcdefghijk
 Output: abcdefghijk12345 67890


void stringcat(char src[], char dest[])
{
int i = 0, j = 0;
for(i; dest[i] != '\0'; i++);
for(j; src[j] != '\0'; i++, j++)
    dest[i] = src[j];

dest[i] = '\0';


}
ฟังก์ชันดังกล่าวจะถูกเรียกใช้ดังลักษณะด้านล่างนี้


int main()
{
  char in1[100],in2[100];

  printf("Input 1: ");
  gets(in1);  /* read a line of characters from the input to "in1" variable */
  printf("Input 2: ");
  gets(in2);  /* read another line of characters from the input to "in2" variable */
  stringcat(in1,in2);
  printf(" Output: ");
  printf("%s\n",in2);
  return 0;
}