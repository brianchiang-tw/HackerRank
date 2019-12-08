# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
def combination_of_k_with_a( letter_list, k):

    comb_list = list( combinations( letter_list, k) )

    comb_with_a = [ comb for comb in comb_list if 'a' in comb ]

    total_combination = len( comb_list )
    valid_combination = len( comb_with_a )

    print( valid_combination / total_combination )

    return


if __name__ == '__main__':


    N = int( input() )
    input_list = list( input().split() )
    k = int( input() )

    combination_of_k_with_a( input_list, k )
