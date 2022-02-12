#include<stdio.h>
#include<conio.h>
int main()
{
      int a=10,b=20,c=21;
      printf(" Enter values of a, b and c");
      printf("\n a = %d",a);
      printf("\n b = %d",b);
      printf("\n c = %d",c);
      a=a+b+c;
      b=a-b-c;
      c=a-b-c;
      a=a-b-c;
      printf("\n After swapping their values are -");
      printf("\n a = %d",a);
      printf("\n b = %d",b);
      printf("\n c = %d",c);
      return 0;
}