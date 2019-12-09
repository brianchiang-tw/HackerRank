#!/bin/python3

import math
import os
import random
import re
import sys

from typing import List

def print_arr_reverse_order( arr:List )->None:
    
    for i in range( len(arr)-1, -1, -1 ):
        print( arr[i], end = ' ')

    return


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print_arr_reverse_order( arr )