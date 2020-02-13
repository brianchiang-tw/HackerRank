#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    // Complete this function    
    int ori_a = *a;
    int ori_b = *b;

    *a = ori_a + ori_b;
    *b = abs(ori_a - ori_b);

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

