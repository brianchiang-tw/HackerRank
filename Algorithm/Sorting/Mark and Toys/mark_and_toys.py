#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):

    prices.sort()

    num_of_pickup = 0
    value_of_pickup = 0
    for x in prices:

        if x + value_of_pickup <= k:

            # within budget, pick one more
            value_of_pickup += x
            num_of_pickup += 1

        else:
            # over budget, break the for loop
            break


    return num_of_pickup


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
