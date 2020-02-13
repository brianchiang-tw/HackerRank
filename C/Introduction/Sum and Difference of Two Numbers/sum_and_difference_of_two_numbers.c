#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int x = 0, y = 0;
    
	scanf("%d %d", &x, &y);
    int sum = x + y;
    int diff = x - y;
    printf("%d %d\n", sum, diff );

    float a = 0, b = 0;
    scanf("%f %f", &a, &b);
    float f_sum = a+b;
    float f_diff = a-b;
    printf("%.1f %.1f\n", f_sum, f_diff );

    return 0;
}

