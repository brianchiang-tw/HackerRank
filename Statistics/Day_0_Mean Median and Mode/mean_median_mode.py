import statistics
from collections import Counter

def stat(arr):

    _mean = sum( arr )/len( arr )

    _median = statistics.median( arr )

    value_occ_dict = Counter( arr )
    #_mode = min( statistics.multimode(arr) )

    max_occ = 0
    _mode_value = 100001

    for value, occ in value_occ_dict.items():
        if occ > max_occ or (occ == max_occ and value < _mode_value):

            max_occ = occ
            _mode_value = value


    print("%.1f" % _mean )
    print("%.1f" % _median )
    print("%d" % _mode_value )

    return


if __name__ == '__main__':

    length_of_arr = int( input() )

    #input_arr = []
    input_arr = list( map( int, input().split() ) )

    stat( input_arr )