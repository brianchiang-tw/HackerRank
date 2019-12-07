from typing import List
from itertools import product

def cartesian_product( list_a:List, list_b:List):

    ctsn_product_of_a_b = list( product(list_a, list_b))

    size = len(ctsn_product_of_a_b)
    for i in range( size ):
        if i != size-1:
            print( ctsn_product_of_a_b[i], end=' ')
        else:
            print( ctsn_product_of_a_b[i], end='')

    return


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':

    list_a = list( map(int, input().split() ) )
    list_b = list( map(int, input().split() ) )

    cartesian_product( list_a, list_b )
