import numpy as np

if __name__ == '__main__':

    arr_a = list( map(int, input().split() ) ) 
    arr_b = list( map(int, input().split() ) )

    np_arr_a = np.array( arr_a )
    np_arr_b = np.array( arr_b )

    # inner product
    print( np.inner(arr_a, arr_b ) )

    # outer product
    print( np.outer(arr_a, arr_b) )

