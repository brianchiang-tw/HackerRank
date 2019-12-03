#!/bin/python3

import math
import os
import random
import re
import sys



def array_left_rotate(n, d, a):


    for i in range(d):

        left_most = a.pop(0)
        a.append( left_most )

    # generate output string as specified
    result_str = " ".join( map(str, a))

    return result_str



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = array_left_rotate(n, d, a)
    print( result )
