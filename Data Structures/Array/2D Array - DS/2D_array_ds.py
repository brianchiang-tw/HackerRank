#!/bin/python3

import math
import os
import random
import re
import sys


def compute_sum_of_hourglass( arr, i, j):
    # i, j is upper-left anchor point of hourglass


    height, width = len(arr), len( arr[0] )

    sum_value = 0

    # boundary checking
    if i < 0 or j < 0 or (i+2) > (height-1) or (j+2) > (width-1):
        return None

    
    sum_value += sum( arr[ i   ][ j:j+3 ] )
    sum_value += sum( arr[ i+2 ][ j:j+3 ] )
    sum_value += arr[ i+1 ][ j+1 ]

    return sum_value


# Complete the hourglassSum function below.
def hourglassSum(arr):

    hourglass = []

    for i in range( len(arr) - 1):
        for j in range( len(arr[0]) - 1) :

            result = compute_sum_of_hourglass(arr, i, j)

            if result is not None:
                hourglass.append( result )
                
    #print( hourglass )
    return max( hourglass )


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
