#!/bin/python3

import math
import os
import random
import re
import sys

def max_of_bit_and( n, k ):

    max_value = ( k-1 if ((k-1) | k) <= n else k-2)
    return max_value


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print( max_of_bit_and(n,k) )