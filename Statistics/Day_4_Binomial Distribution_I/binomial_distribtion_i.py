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
    boy_ratio, girl_ratio = float( buf[0] ), float( buf[1] )

    probability_of_boy = boy_ratio / ( boy_ratio + girl_ratio )

    proportion =    Binomial(3, 6, probability_of_boy) + \
                    Binomial(4, 6, probability_of_boy) + \
                    Binomial(5, 6, probability_of_boy) + \
                    Binomial(6, 6, probability_of_boy)

    print( round(proportion, ndigits = 3) )

# Enter your code here. Read input from STDIN. Print output to STDOUT

