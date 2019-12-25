import numpy as np
from typing import List
def reshpare_to_square_matrix( seq:List)->None:

    square_matrix = np.array( seq )

    # reshpae to square matrix
    square_matrix.shape = (3,3)

    return square_matrix


if __name__ == '__main__':

    int_sequence = list( map( int, input().split() ) )

    # Method_#1
    #sq_matrix = reshpare_to_square_matrix( int_sequence )
    #print( sq_matrix )

    # Method_#2
    sq_matrix = np.array( int_sequence )
    sq_matrix = np.reshape( sq_matrix, (3,3) )
    print( sq_matrix )
    
