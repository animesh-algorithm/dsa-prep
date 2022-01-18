#include <stdio.h>

int reverse(int num, int sum) {
    if (num == 0) return sum;
    sum = sum*10 + num%10;
    return reverse(num/10, sum);
}

int main() {
    int num;
    scanf("%d", &num);
    int result = reverse(num, 0);
    printf("%d", result);
    return 1;
}