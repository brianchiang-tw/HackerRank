#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the matchingStrings function below.
def matchingStrings(strings, queries):

    str_occ_dictionary = Counter( strings )

    look_up_answer = []

    for q in queries:

        occurrence_of_q = str_occ_dictionary.get(q, 0)
        look_up_answer.append( occurrence_of_q )

    return look_up_answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
