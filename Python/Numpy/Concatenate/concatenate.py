import numpy as np

if __name__ == '__main__':

    n, m, p = map( int, input().split() )

    matrix = None

    for i in range( n ):

        if i == 0:
            matrix = np.zeros( shape = (1,p), dtype = np.int )

            row_elements = list( map( int, input().split() ) )

            for j in range(p):
                matrix[0][j] = row_elements[j]

        else:
            buf = np.zeros( shape = (1,p), dtype = np.int )
            
            row_elements = list( map( int, input().split() ) )

            for j in range(p):
                buf[0][j] = row_elements[j]

            matrix = np.concatenate( (matrix, buf), axis = 0 )



    for i in range( m ):

        buf = np.zeros( shape = (1,p), dtype = np.int )
        
        row_elements = list( map( int, input().split() ) )

        for j in range(p):
            buf[0][j] = row_elements[j]

        matrix = np.concatenate( (matrix, buf), axis = 0 )


    print( matrix )
