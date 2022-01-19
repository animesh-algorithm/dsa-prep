#include<stdio.h>

void swap(int *,int *);

int main() {
    int a=10, b=20;
    printf("%d %d\n", a, b);
    swap(&a, &b);
    printf("%d %d\n", a, b);
    return 1;
}
void swap(x,y)
int *x,*y;
{
	int t;
	t=*x;
	*x=*y;
	*y=t;
}