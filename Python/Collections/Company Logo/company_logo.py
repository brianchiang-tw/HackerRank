#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def top_3_char_occ( s ):

    char_occ_dict = dict( Counter(s) )

    
    # first order: occurrence
    # second order: alphabet lexical order
    top_3_char_occ \
    = sorted( char_occ_dict.items(), key = lambda x: (x[1], -ord(x[0]) ), reverse = True )[0:3]

    

    for x in top_3_char_occ:
        print(f'{x[0]} {x[1]}')

    return

if __name__ == '__main__':
    s = input()

    top_3_char_occ( s)
