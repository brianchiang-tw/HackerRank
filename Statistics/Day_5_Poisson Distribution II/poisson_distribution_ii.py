# Enter your code here. Read input from STDIN. Print output to STDOUT
def expectation_of_square( avg ):

    # E[x^2]    =   Var(x) + ( E[X])^2
    #           =   lambda + lambda^2

    return ( avg + avg**2 )



if __name__ == '__main__':

    buf = list( map( float, input().split() ) )

    avg_of_A, avg_of_B = buf[0], buf[1]

    cost_of_a = 160 + 40 * expectation_of_square( avg_of_A )
    cost_of_b = 128 + 40 * expectation_of_square( avg_of_B )

    print( round(cost_of_a, 3) )
    print( round(cost_of_b, 3) )
