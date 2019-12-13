#!/bin/python3

import math
import os
import random
import re
import sys

def length_of_consecutive_ones( n ):

    # Convert n to binary string
    num_str = "{:b}".format(n)

    # Match at least one '1'
    pattern = re.compile( "[1]{1,}") 

    # find all match case
    ones = re.findall(pattern, num_str)

    # get the longest one
    max_len_of_cont_ones = max( ones, key = len)
    
    # print the length of longest one
    print( len(max_len_of_cont_ones))

    

if __name__ == '__main__':
    n = int(input())

    length_of_consecutive_ones( n )
