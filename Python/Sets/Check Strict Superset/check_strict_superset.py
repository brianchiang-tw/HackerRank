# Enter your code here. Read input from STDIN. Print output to STDOUT
from typing import Set

def is_strict_superset( set_A:Set, set_B:Set )->bool:

    if set_B.issubset( set_A ) and len(set_A) > len(set_B):
        return True

    else:
        return False



if __name__ == '__main__':

    set_A = set( map( int, input().split() ) )

    times_of_query = int( input() )

    for _ in range( times_of_query ):

        set_B = set( map(int, input().split() ) )

        chk_flag = is_strict_superset(set_A, set_B)

        if chk_flag is False:
            print("False")
            break
    else:
        # if all cases is pass with strict super-set checking
        print("True")