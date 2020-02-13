#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  

    char s[1024]={0};

    for(int i = 0 ; i < 3 ; i ++){
        scanf("%[^\n]%*c", s);
        printf("%s\n", s);
    
    }
    return 0;
}

