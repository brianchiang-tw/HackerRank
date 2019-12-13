#!/bin/python3

import math
import os
import random
import re
import sys

def athlete_sort( arr, k):

    arr.sort( key = lambda x: x[k] )

    for athlete_record in arr:
        
        output_str = ' '.join( map(str, athlete_record) )
        print(output_str)


    return

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    athlete_sort( arr, k )
