def geometric_prob(n, p):

    q = ( 1- p )

    geo_n_p = ( q ** (n-1) ) * ( p ** 1 )

    return geo_n_p



if __name__ == '__main__':

    buf = list( map( int, input().split() ) )

    defect_rate = buf[0] / buf[1]

    n = int( input() )

    geo_n_defect_date = 0

    for i in range( 1, n+1):
        geo_n_defect_date += geometric_prob(i, defect_rate)

    print( round(geo_n_defect_date, 3) )