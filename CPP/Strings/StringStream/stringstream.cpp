#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    stringstream ss(str);
    vector<int> sequence;
    int x = 0;
    char sep = '\0';
    
    while( ss.good() )
    {
        if( sep == '\0' )
        {
            ss >> x;
            sequence.push_back( x );
            sep = ',';
        }
        else
        {
            ss >> sep;
            sep = '\0';

        }

    }
    
    return sequence;

}
//end of function parseInts

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}

