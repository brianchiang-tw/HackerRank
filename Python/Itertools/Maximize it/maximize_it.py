# Enter your code here. Read input from STDIN. Print output to STDOUT
from typing import List
from itertools import product

def sum_of_square_mod_m( nums:tuple, mod_m ):

    return ( sum( map( lambda x: x**2, nums) ) % mod_m )



def maximize_function_value( list_of_list:List , mod_m):

    count_of_list = len( list_of_list )

    all_possible_combination = list( product( *list_of_list ) )

    max_fn_value = -1

    for one_trial in all_possible_combination:

        # update max function value
        max_fn_value = max(sum_of_square_mod_m( one_trial, mod_m ), max_fn_value)

    
    print( max_fn_value )


if __name__ == '__main__':

    buf = list( map( int, input().split() ) )
    k, m = buf[0], buf[1]

    list_of_list = []

    for _ in range(k):
        list_of_list.append( list( map( int, input().split() ) )[1:] )

    maximize_function_value( list_of_list, m )
