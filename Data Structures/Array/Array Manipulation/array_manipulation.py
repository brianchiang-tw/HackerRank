#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [ 0 ] * n

    for q in queries:

        left, right, adder = q[0]-1, q[1]-1, q[2]

        for i in range( left, right+1):
            array[i] = array[i] + adder

    max_element = max( array )
    #print(" array : {}".format( array ) )

    return max_element


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
