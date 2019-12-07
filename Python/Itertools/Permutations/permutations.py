# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

def permutation_of_2( s:str, degree ):

    result = list( permutations( s, degree) )

    result.sort()

    for entry in result:
        print(''.join(entry) )

    return



if __name__ == '__main__':

    buf = input().split()
    input_string, n = buf[0], int(buf[1])

    permutation_of_2( input_string, n )