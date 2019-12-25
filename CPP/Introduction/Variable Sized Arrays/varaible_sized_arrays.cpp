#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    
    vector< vector<int> > pool_of_array;

    int n=0, q =0;

    cin >> n >> q;

    for( int i = 0 ; i < n ; i ++ )
    {
        int length = 0;
        cin >> length;

        vector<int> arr;

        for( int j = 0 ; j < length ; j++)
        {
            int buf = 0;

            cin >> buf;
            arr.push_back( buf );
            

        }
        //end of for loop j
        pool_of_array.push_back(arr);

    }
    //end of for loop i

    for( int k = 0 ; k < q ; k++ )
    {
        int index_of_vec = 0;
        int position_of_seq = 0;

        cin >> index_of_vec >> position_of_seq;

        cout << pool_of_array[index_of_vec][position_of_seq] << endl;

    }
    //end of for loop k

    return 0;
}

