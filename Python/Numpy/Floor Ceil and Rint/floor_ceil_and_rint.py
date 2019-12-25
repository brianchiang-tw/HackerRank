import numpy as np

if __name__ == '__main__':
    
    list_of_float = list( map(float, input().split() ) ) 

    array_a = np.array( list_of_float )

    # to enable wider print option for output format alignment on the Online Judge
    np.set_printoptions(legacy='1.13')

    print( np.floor( array_a) )
    print( np.ceil( array_a) )
    print( np.rint( array_a) )