#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):

    token_list = list( s.split() )

    output_str = str()

    end_of_prev_token, i = 0, 0
    while 0 != len(token_list):
        # pop the first token
        token = token_list.pop(0)
        

        # get the start index of token
        index_of_token = s.find(token, end_of_prev_token)

        # padding space
        space_char = " "*( index_of_token - end_of_prev_token )
        output_str += space_char

        # update index of prev token for next run
        end_of_prev_token = index_of_token + len(token)

        if s[index_of_token].isalpha():

            output_str += token[0].upper() + token[1:]
        
        else:

            output_str += token

    

    #print( output_str )

    return output_str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
