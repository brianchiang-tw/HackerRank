#include <stdio.h>
#include <cmath>

void update(int *a,int *b) {
    // Complete this function    
    int s = *a + *b;
    int abs_diff = abs( *a - *b );

    *a = s;
    *b = abs_diff;

    return;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

