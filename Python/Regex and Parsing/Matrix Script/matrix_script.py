#!/bin/python3

import math
import os
import random
import re
import sys

regex = r'(?<=\w)(\W+)(?=\w)'
pattern = re.compile(regex)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)



list_str = [ ''.join(t)  for t in zip(*matrix) ]
original_str = ''.join(list_str)
#print( original_str )

output_str = pattern.sub(' ', original_str)
print( output_str )

