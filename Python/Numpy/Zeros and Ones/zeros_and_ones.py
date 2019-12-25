import numpy as np


if __name__ == '__main__':

    dim = list(map( int, input().split() ) ) 


    zero_matrix = np.zeros( shape = tuple(dim) , dtype = np.int )
    one_matrix = np.ones( shape = tuple(dim) , dtype = np.int )



    print(zero_matrix)
    print(one_matrix )