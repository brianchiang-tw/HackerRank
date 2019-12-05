

def get_median( arr ):

    size = len(arr)
    mid_pos = size // 2


    if size % 2 == 0:
        # size is even

        median = ( arr[mid_pos-1] + arr[mid_pos] ) / 2

    else:
        # size is odd
        median = arr[mid_pos]

    return int(median)


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


    print(Q1)
    print(Q2)
    print(Q3)

    return


if __name__ == '__main__':
# Enter your code here. Read input from STDIN. Print output to STDOUT
    N = int( input() )

    #input_str = input()
    #print("input data:", input_str)
    arr = list( map(int, input().rstrip().split() ) )

    collect_Q1_Q2_Q3( arr )
