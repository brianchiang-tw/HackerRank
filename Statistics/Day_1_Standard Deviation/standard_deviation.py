
def get_average( arr ):

    return sum( arr )/len( arr )



def get_std( arr ):
    # for root square
    from math import sqrt

    miu = get_average(arr)

    square_diff = sum( [ ( (x-miu)**2 ) for x in arr ] )

    std = sqrt( square_diff/len(arr) )

    return std



if __name__ == '__main__':
# Enter your code here. Read input from STDIN. Print output to STDOUT
    
    n = int( input() )

    num_arr = list( map(int, input().rstrip().split() ) )

    std = get_std( num_arr )

    print( "%.1f" % std )