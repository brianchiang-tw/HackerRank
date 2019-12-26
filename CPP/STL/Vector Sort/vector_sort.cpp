#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 

    int n = 0 ;
    vector<int> sequence;

    cin >> n;

    for( int i = 0 ; i < n ; i ++)
    {
        int elem = 0;
        cin >> elem;
        sequence.push_back( elem );

    }

    sort( sequence.begin(), sequence.end() );

    for( auto it = sequence.begin() ; it != sequence.end() ; it ++ )
    {
        printf("%d ", *it);
    }

    return 0;
}
