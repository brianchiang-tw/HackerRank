import numpy as np

if __name__ == '__main__':

    h, w = map( int, input().split() )

    row_list = []

    for i in range(h):

        single_row = list( map(int, input().split() ) ) 

        np_row = np.array( single_row )

        row_list.append( np_row )


    min_of_each_row = np.min( row_list, axis = 1)

    max_of_min = np.max( min_of_each_row )

    print( max_of_min )


