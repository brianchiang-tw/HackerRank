
def get_median( arr ):

    size = len(arr)
    mid_pos = size // 2


    if size % 2 == 0:
        # size is even

        median = ( arr[mid_pos-1] + arr[mid_pos] ) / 2

    else:
        # size is odd
        median = arr[mid_pos]

    return (median)



def collect_Q1_Q2_Q3( arr ):

    # Preprocessing
    # in-place sorting
    arr.sort()

    Q2 = get_median( arr )

    size = len(arr)
    mid = size // 2

    if size % 2 == 0:
        # size is even
        Q1 = get_median( arr[:mid] )
        Q3 = get_median( arr[mid:] )

    else:
        # size is odd
        Q1 = get_median( arr[:mid]   )
        Q3 = get_median( arr[mid+1:] )




    return (Q1, Q2, Q3)


def expand_to_flat_list( element_arr, freq_arr ):

    flat_list = []

    for index in range( len(element_arr) ):

        cur_element = element_arr[ index ]
        cur_freq = freq_arr[ index ]

        # repeat current element with cur_freq times
        cur_list = [ cur_element ] * cur_freq

        flat_list += cur_list

    
    return flat_list



def get_interquartile_range( arr ):

    Q1, Q2, Q3 = collect_Q1_Q2_Q3( arr )

    return (Q3-Q1)



if __name__ == '__main__':
# Enter your code here. Read input from STDIN. Print output to STDOUT

    n = int( input() )

    element_arr = list( map(int, input().strip().split() ) )
    frequency_arr = list( map(int, input().strip().split() ) )

    flat_list = expand_to_flat_list( element_arr, frequency_arr)

    inter_quartile_range = get_interquartile_range( flat_list )

    print( "%.1f" % inter_quartile_range )
