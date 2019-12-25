#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)


class Box
{
    private:
        int _length;
        int _breadth;
        int _height;


    public:
        Box():_length( 0 ),_breadth( 0 ), _height( 0 ){}

        Box(int l, int b, int h):_length( l ),_breadth( b ), _height( h ){}

        Box(Box& b)
        {
            this->_length     =  b.getLength() ;
            this->_breadth    =  b.getBreadth() ;
            this->_height     =  b.getHeight() ;
        }

        int getLength(){ return this->_length; }
        int getBreadth(){ return this->_breadth; }
        int getHeight(){ return this->_height; }
        long long CalculateVolume(){ return ( (long)_length * _breadth * _height); }

        

        bool operator<(Box& b)
        {
            if( _length < b.getLength() )
            {
                return true;
            }
            else if( _length == b.getLength() && _breadth < b.getBreadth() )
            {
                return true;
            }
            else if( _length == b.getLength() && _breadth == b.getBreadth() && _height < b.getHeight() )
            {
                return true;
            }
            return false;
        }

        friend ostream& operator<<(ostream& out, Box& B);


};
//end of definition of class Box




ostream& operator<<(ostream& out, Box& B)
        {
            out << B.getLength() << " " << B.getBreadth() << " " << B.getHeight() ;
            return out;
        }


void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}