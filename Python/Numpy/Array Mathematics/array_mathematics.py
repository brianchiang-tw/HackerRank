import numpy as np

def assign_matrix( arr ):

    for i in range(h):

        row_elements = list( map(int, input().split() ) )

        for j in range(w):

            arr[i][j] = row_elements[j]


    return



if __name__ == '__main__':

    h, w = map( int, input().split() )

    a = np.zeros( shape = (h,w), dtype = np.int )
    b = np.zeros( shape = (h,w), dtype = np.int )

    assign_matrix( a )
    assign_matrix( b )

    print( a+b )
    print( a-b )
    print( a*b )
    print( a//b )
    print( a%b )
    print( a**b )
            


