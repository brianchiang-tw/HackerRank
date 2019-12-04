#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#




def create_continuous_sum(a, limit):

    Cont_sum = [ a[0] ]

    for element in a[1:]:

        accumulation = element + Cont_sum[-1]

        if accumulation <= limit:

            # extend Cont_Sum as long as possible and keeps not greater than limit
            Cont_sum += [accumulation]
        else:
            # larger than limit, break and retrun
            break


    return list(Cont_sum)


def valid_pickup( sum_a, sum_b, sentry_a, sentry_b, limit ):

    if sum_a[sentry_a] + sum_b[sentry_b] <= limit:
        return True
    
    else:
        return False



def twoStacks(x, a, b):

    limit = x

    if min(a[0], b[0]) > limit:
        # corner case, minimum of stack a and stack b is greater then limit,
        # no solution of pickup
        return 0
    
 
    Cont_Sum_a, Cont_Sum_b = create_continuous_sum(a, limit), create_continuous_sum(b, limit)


    if len(Cont_Sum_a) < len(Cont_Sum_b) : 

        # let Cont_Sum_a be the shorter one
        Cont_Sum_a, Cont_Sum_b = Cont_Sum_b, Cont_Sum_a


    sentry_a, sentry_b, max_pickup = len(Cont_Sum_a)-1, 0, 0

    while sentry_a >= 0:
        # sentry_a scan from tail to head in Cont_Sum_a

        while sentry_b < len(Cont_Sum_b) and valid_pickup( Cont_Sum_a, Cont_Sum_b, sentry_a, sentry_b, limit):
            # sentry_b scan from head to tail in Cont_Sum_b
            # sentry_b go as further as possible
            sentry_b += 1
        
        max_pickup = max( max_pickup, (sentry_a + 1) + sentry_b )

        # sentry_a move backward
        # this means pop lastest pick-up element from a to spare more space for element in b
        sentry_a -= 1

    return max_pickup





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
