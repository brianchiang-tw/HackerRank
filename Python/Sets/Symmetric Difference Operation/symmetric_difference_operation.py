from typing import Set

def symm_diff_of_set( set_a:Set, set_b:Set)->Set:

    # equal to
    # symm_diff_set = set_a.symmetric_difference( set_b )
    symm_diff_set = set_a ^ set_b

    return symm_diff_set


# Enter your code here. Read input from STDIN. Print output to STDOUT

n, en_subscriber = int( input() ), set( map(int, input().split() ) )
b, fr_subscriber = int( input() ), set( map(int, input().split() ) )

set_of_either_en_or_fr_but_not_both = symm_diff_of_set( en_subscriber, fr_subscriber)

print( len(set_of_either_en_or_fr_but_not_both) ) 