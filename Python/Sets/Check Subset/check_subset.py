from typing import Set

def is_A_a_subset_of_B( set_A:Set, set_B:Set)->bool:

    return set_A.issubset( set_B)


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':

    number_of_query = int( input() )

    for _ in range( number_of_query ):

        size_A, set_A, size_B, set_B =  int( input() ), \
                                        set( map( int, input().split() ) ), \
                                        int( input() ), \
                                        set( map( int, input().split() ))

        print( is_A_a_subset_of_B( set_A, set_B ) )
