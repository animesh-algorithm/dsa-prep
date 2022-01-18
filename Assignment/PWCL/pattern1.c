#include <stdio.h>

void pattern(int N) {
    if (N==0) return;
    pattern(N-1);
    helper(N);
    printf("\n");
}

void helper(int N) {
    if (N==0) return;
    printf("*");
    helper(N-1);
}

int main() {
    pattern(5);
    return 1;
}