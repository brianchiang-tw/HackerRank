import numpy as np

if __name__ == '__main__':

    dim = int(input())

    arr_a = []
    arr_b = []

    for i in range(dim):

        arr_a += list( map(int, input().split() ) ) 

    for i in range(dim):

        arr_b += list( map(int, input().split() ) ) 


    np_arr_a = np.array( arr_a)
    np_arr_a = np.reshape( np_arr_a, (dim, dim) )

    np_arr_b = np.array( arr_b)
    np_arr_b = np.reshape( np_arr_b, (dim, dim) )

    print( np.matmul(np_arr_a, np_arr_b) )
    



