#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):


    index, swap_count = 0, 0

    # key concept:
    # a sorted array of this problem must follow this property that arr[index] = index+1
    while index < len(arr):

        if arr[index] == (index+1):
            # match

            index += 1
            continue
        
        else:
            # swap arr[index], arr[ arr[index]-1 ]
            # in order to send arr[index] to its destination with index-1
            index_of_dest = arr[index]-1
            arr[index], arr[ index_of_dest ] = arr[ index_of_dest ], arr[index]

            # update swap count
            swap_count += 1



    return swap_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
