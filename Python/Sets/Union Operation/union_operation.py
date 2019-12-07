from typing import Set

def union_of_set( set_a:Set, set_b:Set)->Set:

    union_set = set_a.union( set_b )

    return union_set


# Enter your code here. Read input from STDIN. Print output to STDOUT

n, en_subscriber = int( input() ), set( map(int, input().split() ) )
b, fr_subscriber = int( input() ), set( map(int, input().split() ) )

set_of_either_en_or_fr = union_of_set( en_subscriber, fr_subscriber)

print( len(set_of_either_en_or_fr) ) 