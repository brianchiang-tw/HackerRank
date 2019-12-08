# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement
def comb_with_replacement( s, k):

    # reorder all character of s in lexical order
    s = ''.join( sorted(s))

    comb_list = combinations_with_replacement(s, k)

    for comb in comb_list:

        print( ''.join(comb) )

    return



if __name__ == '__main__':

    buf = list( input().split() )

    s, k = buf[0], int( buf[1] )

    comb_with_replacement( s, k )