import numpy as np



if __name__ == '__main__':

    h, w = map( int, input().split() )

    # create a zero matrix of shape h x w
    matrix = np.zeros( shape = (h, w), dtype = np.int )

    for i in range(h):

        row_elements = list( map(int, input().split() ) )

        for j in range(w):
            matrix[i][j] = row_elements[j]
            

    # Task_#1: Matrix Transpose
    matrix_transpose = np.transpose( matrix )
    print( matrix_transpose )



    # Task_#2: Matrix Flatten
    matrix_flatten = matrix.flatten( )
    print( matrix_flatten )

