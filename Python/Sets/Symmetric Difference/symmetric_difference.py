# Enter your code here. Read input from STDIN. Print output to STDOUT

from typing import Set

def print_set( x:Set )->None:

    list_of_set = list( x )
    list_of_set.sort()
    
    for element in list_of_set:
        print(element)

    return



def gen_symm_difference( set_a:Set, set_b:Set )->Set:

    union_of_a_b = set_a.union(set_b)

    intersection_of_a_b =set_a.intersection(set_b)

    symmetric_difference = union_of_a_b.difference( intersection_of_a_b )

    return symmetric_difference



if __name__ == '__main__':

    M = int( input() )

    set_a = set( map(int, input().split() ) ) 

    N = int( input() )

    set_b = set( map(int, input().split() ) )

    print_set( gen_symm_difference(set_a, set_b) )

