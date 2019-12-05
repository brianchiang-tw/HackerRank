#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):

    count_of_swap = 0
    for i in range( len(a) ):
        for j in range( len(a)-1 ):

            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count_of_swap += 1

    print("Array is sorted in {} swaps.".format(count_of_swap) )
    print("First Element: {}".format(a[0]) )
    print("Last Element: {}".format(a[-1]) )

    return


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
