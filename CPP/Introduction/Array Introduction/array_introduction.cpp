#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int arr[1000] = {0};
    int n = 0;

    cin >> n;

    for( int i = n-1 ; i >=0 ; i--)
    {
        int buf = 0 ;
        cin >> buf;
        arr[i] = buf;

    }

    for( int i = 0; i < n ; i++ )
    {
        printf("%d ", arr[i]);
    }

    return 0;
}
