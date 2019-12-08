# Enter your code here. Read input from STDIN. Print output to STDOUT
def geometric_prob(n, p):

    q = ( 1- p )

    geo_n_p = ( q ** (n-1) ) * ( p ** 1 )

    return geo_n_p



if __name__ == '__main__':

    buf = list( map( int, input().split() ) )

    defect_rate = buf[0] / buf[1]

    n = int( input() )

    geo_n_defect_date = geometric_prob(n, defect_rate)

    print( round(geo_n_defect_date, 3) )

