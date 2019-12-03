#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    
    sequence_list = [ [] for i in range(0, n) ]

    last_asnwer = 0

    result_str = []

    for q in queries:


        type_of_q, x, y = q[0], q[1], q[2]

        if type_of_q == 1:

            index_of_seq = ( (x ^ last_asnwer) %n )

            # append integer y to speficied sequence
            sequence_list[ index_of_seq ].append( y )


        elif type_of_q == 2:

            index_of_seq = ( (x ^ last_asnwer) %n )

            size = len( sequence_list[index_of_seq] )
            
            # Find the value of element ( y mod size ) in seq, and assign it to last answer
            new_value = sequence_list[index_of_seq][ y % size ]

            last_asnwer = new_value

            print( new_value )
            result_str.append( new_value )

    return result_str

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
