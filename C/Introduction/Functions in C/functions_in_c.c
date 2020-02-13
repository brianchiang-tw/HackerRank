#include <stdio.h>
#include <stdlib.h>

#ifndef max
#define max(a,b)            (((a) > (b)) ? (a) : (b))
#endif
/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int max_of_four( int a, int b, int c, int d)
{
    return max( a, max(b, max(c, d) ) );
}
//end of function max_of_four


int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

