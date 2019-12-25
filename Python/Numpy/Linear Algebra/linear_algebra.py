import numpy as np

if __name__ == '__main__':

    dim = int( input() )

    arr = []

    for i in range(dim):

        arr += list( map(float, input().split() ) )

    np_arr = np.array( arr )
    np_arr = np.reshape( np_arr, (dim, dim) )
    determine = np.linalg.det(np_arr)

    np.set_printoptions(legacy='1.13')
    print(  determine  )
    





