#!/bin/python3

import math
import os
import random
import re
import sys


regex = r'^([a-z]{1,20}) ([a-z@\.]{1,50})@gmail.com$'
pattern = re.compile( regex )

first_name_list = []

def parse_string( s ):

    matching = re.match( pattern, s)

    if matching:
        first_name_list.append( matching.group(1) )
    

if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):

        input_str = input()

        parse_string( input_str )


    first_name_list.sort()

    for fn in first_name_list:
        print( fn )