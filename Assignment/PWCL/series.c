#include <stdio.h>
#include<math.h>
long factorial(int p)
{
	long f = 1;
	for (p; p>=1; p--)
		f *= p;
	return f;
}

float series(float x)
{
	float sum = 0;
	int i, s = 1;
	for (i = 1; i <= 9; i += 2)
	{
		sum += (pow((double) x, i) / factorial(i))*s;
		s *= -1;
	}
	return sum;
}

int main( )
{
	int x=10;
	printf("enter the value of x: ");
	// scanf("%d", &x);
	printf("\nAns: %f\n", series(x));
	
	return 0;
}