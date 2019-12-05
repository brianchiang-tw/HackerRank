#!/bin/python3

import math
import os
import random
import re
import sys


def _merge( arr, left, mid, right):

    # in-place merge
    left_part = arr[left: mid+1]
    right_part = arr[mid+1:right+1]
    
    left_index, right_index = 0, 0

    insertion_index = left
    inversion_count = 0

    while left_index != (mid-left+1) and right_index != (right-mid):

        if left_part[left_index] <= right_part[right_index]:
            # head element of left_part is smaller

            arr[insertion_index] = left_part[left_index]
            left_index += 1
            insertion_index += 1
        
        else:
            # head element of right_part is smaller

            arr[insertion_index] = right_part[right_index]
            right_index += 1
            insertion_index += 1

            # update inversion count
            # all the remaing elements in left_part is larger than right_part[0]
            inversion_count += (mid - left - left_index + 1)


    while left_index != (mid-left+1):
        # rihgt part is empty, dump all left part to arr
        arr[insertion_index] = left_part[left_index]
        left_index += 1
        insertion_index += 1
    
    while right_index != (right-mid):
        # left part is empty, dump all right part to arr
        arr[insertion_index] = right_part[right_index]
        right_index += 1
        insertion_index += 1

    return inversion_count



def merge_sort(arr, left, right):

    if left == right:
        return 0

    mid = (left + right) // 2

    inversion_count = 0

    if( right > left ):

        
        # Divide state: left part
        inversion_count += merge_sort(arr, left, mid)

        # Divide stage: left part
        inversion_count += merge_sort(arr, mid+1, right)

        # Conquer state: merge left and right
        inversion_count += _merge(arr, left, mid, right)

    return inversion_count



# Complete the countInversions function below.
def countInversions(arr):

    is_strictly_descreasing = all(i > j for i, j in zip( arr, arr[1:] ) ) 

    if is_strictly_descreasing:
        n = len(arr)

        return n*(n-1)//2


    return merge_sort(arr, 0, len(arr)-1)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
