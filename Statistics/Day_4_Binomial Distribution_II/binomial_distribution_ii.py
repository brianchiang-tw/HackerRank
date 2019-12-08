# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial

def C(n, m):

    if m == 0:
        return 1

    else:

        return factorial(n) // ( factorial(m) * factorial(n-m) )


def Binomial(x, n, p):

    q = ( 1 - p )
    return C(n,x) * (p ** x) * ( q ** ( n-x) )



if __name__ == '__main__':

    buf = input().split()
    fail_rate, n = int( buf[0] ), int( buf[1] )
    fail_rate = fail_rate / 100
    ans_1 = Binomial( 0, n, fail_rate) + \
            Binomial( 1, n, fail_rate) + \
            Binomial( 2, n, fail_rate)

    print( round(ans_1, ndigits = 3) )



    less_than_two_fail =    Binomial( 0, n, fail_rate) + \
                            Binomial( 1, n, fail_rate)

    ans_2 = 1 - less_than_two_fail
    print( round(ans_2, ndigits = 3) )


