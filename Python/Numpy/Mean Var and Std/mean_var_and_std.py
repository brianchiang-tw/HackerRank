import numpy as np

if __name__ == '__main__':

    h, w = map( int, input().split() )

    row_list = []

    for i in range(h):

        single_row = list( map(int, input().split() ) )

        row_list.append( single_row )

    # enable legacy output mode
    np.set_printoptions( legacy = '1.13' )

    print( np.mean(row_list, axis = 1) )
    print( np.var(row_list, axis = 0 ) )
    print( np.std(row_list) )




