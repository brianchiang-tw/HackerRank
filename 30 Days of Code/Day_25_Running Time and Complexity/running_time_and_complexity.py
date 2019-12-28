# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import ceil

def judge_prime( num ):

    if num == 1:
        return False

    if num == 2:
        return True

    
    num_sqrt = ceil( num**0.5 )

    for i in range( 2, num_sqrt+1 ):

        if num % i == 0:
            return False

    
    return True


if __name__ == '__main__':

    q = int( input() )

    for _ in range(q):

        x = int( input() )

        if judge_prime( x ) :
            print("Prime")

        else:
            print("Not prime")
