# Enter your code here. Read input from STDIN. Print output to STDOUT
from typing import Set
def intersect_of_set( set_a:Set, set_b:Set)->Set:

    intersection = set_a.intersection(set_b)

    return intersection

if __name__ == '__main__':

    n, english_subscriber = int(input()), set( map(int, input().split() ) )
    b, french_subscriber = int(input()), set( map(int, input().split() ) )

    eng_fr_subscriber = intersect_of_set( english_subscriber, french_subscriber)

    print( len(eng_fr_subscriber) )
