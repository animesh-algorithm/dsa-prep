#include<stdio.h>

void generatePattern(int R, int C) {
    int i, j, k;
    for (i=0; i<=R; i++) {
        k=1;
        for (j=0; j<=C; j++) {
            if (j >= C-i-2 && j <= i+3) {
                if (k==1) {
                    printf("*");
                    k=0;
                } else {
                    printf(" ");
                    k=1;
                }
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
    generatePattern(4,7);
    return 1;
}

//     *   
//    * *  
//   * * * 
//  * * * *