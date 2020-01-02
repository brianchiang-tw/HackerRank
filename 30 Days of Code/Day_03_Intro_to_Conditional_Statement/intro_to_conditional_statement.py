#!/bin/python3

import math
import os
import random
import re
import sys



def is_weird( num ):

    if num%2 == 1:
        # odd
        print("Weird")

    else:
        # even
        if 5 >= num >= 2:
            print("Not Weird")

        elif 20 >= num >= 6:
            print("Weird")
        
        else:
            print("Not Weird")


    return


'''
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6  to 20, print Weird
If  is even and greater than 20, print Not Weird

'''



if __name__ == '__main__':
    N = int(input())
    is_weird( N )
