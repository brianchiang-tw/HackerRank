from math import factorial
from math import e


def poisson_distribution( avg, k):

    p_k_lambda = ( ( avg**k ) * ( e ** (-avg) ) ) / factorial(k)

    return p_k_lambda



if __name__ == '__main__':

    avg = float( input() )

    k = float( input() )

    print( round( poisson_distribution(avg, k), 3) )