import numpy as np

if __name__ == '__main__':

    h, w = map( int, input().split() )

    matrix_I = np.eye(h, w, k = 0, dtype = np.float )

    # to enable wider print option for output format alignment on the Online Judge
    np.set_printoptions(legacy='1.13')
    print( matrix_I )


