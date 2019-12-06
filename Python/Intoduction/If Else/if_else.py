#!/bin/python3

import math
import os
import random
import re
import sys


def judge_n( x ):

    if x % 2 == 1:
        # odd
        print("Weird")

    else:
        # even
        if 5 >= x >= 2:
            print("Not Weird")

        elif 20>= x >= 6:
            print("Weird")
        
        else:
            print("Not Weird")


    return


if __name__ == '__main__':
    n = int(input().strip())

    judge_n( n )

