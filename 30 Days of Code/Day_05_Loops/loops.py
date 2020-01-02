#!/bin/python3

import math
import os
import random
import re
import sys

def product_of_n( n ):
        
    for i in range( 1, 11):
        print( f"{n} x {i} = {n*i}" )


    return 

if __name__ == '__main__':
    n = int(input())

    product_of_n( n )
