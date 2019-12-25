#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student{
    private:
        int _age;
        string _first_name;
        string _last_name;
        int _standard;

    public:

        void set_age( int age)
        {
            _age = age;
        }

        int get_age()
        {
            return _age;
        }

        void set_standard( int st)
        {
            _standard = st;
        }

        int get_standard()
        {
            return _standard;
        }

        void set_first_name( string fn )
        {
            _first_name = fn;
        }

        string get_first_name()
        {
            return _first_name;
        }

        void set_last_name( string ln )
        {
            _last_name = ln;
        }

        string get_last_name()
        {
            return _last_name;
        }

        string to_string()
        {
            string outstr =  std::to_string(_age) + "," + _first_name + "," + _last_name + "," + std::to_string(_standard) + "\n";
            return outstr;
        }

};


int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}

