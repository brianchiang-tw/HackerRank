#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

def read_datetime( s ):
    return datetime.datetime.strptime(s, '%a %d %b %Y %H:%M:%S %z')

# Complete the time_delta function below.
def time_delta(t1, t2):

    t1_time = read_datetime( t1 )
    t2_time = read_datetime( t2 )

    diff = t1_time - t2_time

    print( diff.total_seconds() )

    return int( abs( diff.total_seconds() )  )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write( str(delta) + '\n')

    fptr.close()
