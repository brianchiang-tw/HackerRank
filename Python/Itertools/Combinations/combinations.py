# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

def element_combination( s, num_of_pick):

    list_of_comb = []

    # re-arrange all letters of s in lexical order
    s =''.join(sorted(s))


    for i in range(1, num_of_pick+1):
        list_of_comb += list( combinations(s, i) )

    

    for c in list_of_comb:
        print(''.join(c) )

    return
    

if __name__ == '__main__':

    buf = list( input().split() )

    s, n = buf[0], int( buf[1] )

    element_combination(s, n)