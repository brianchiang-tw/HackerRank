#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

total_number_of_swap = 0

for i, x in enumerate( a ):

    cur_number_of_swap = 0

    for j in range( len(a) -1 ):

        if a[j] > a[j+1]:

            a[ j ], a[ j+1 ] = a[ j+1 ], a[ j ]
        
            cur_number_of_swap += 1

    # update totla number of swap
    total_number_of_swap += cur_number_of_swap
    
    if cur_number_of_swap == 0:

        # no more inversion, swap is accomplished
        break


print(f'Array is sorted in {total_number_of_swap} swaps.'
)

print(f'First Element: {a[0]}')
print(f'Last Element: {a[len(a)-1]}')