from typing import Set

def difference_of_set( set_a:Set, set_b:Set)->Set:

    diff_set = set_a.difference( set_b )

    return diff_set


# Enter your code here. Read input from STDIN. Print output to STDOUT

n, en_subscriber = int( input() ), set( map(int, input().split() ) )
b, fr_subscriber = int( input() ), set( map(int, input().split() ) )

set_of_en_only = difference_of_set( en_subscriber, fr_subscriber)

print( len(set_of_en_only) ) 