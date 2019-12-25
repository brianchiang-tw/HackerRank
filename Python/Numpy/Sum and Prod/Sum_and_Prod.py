import numpy as np

if __name__ == '__main__':

    h, w = map( int, input().split() )

    array_a = []

    for i in range(h):
        array_a += list( map( int, input().split() ) ) 

    
    np_arr_a = np.array( array_a, dtype = np.int )
    np_arr_a = np.reshape( np_arr_a, (h,w) )

    sum_over_axis_0 = np.sum( np_arr_a, axis = 0 )

    product_over_sum = np.product( sum_over_axis_0 )

    print( product_over_sum )


