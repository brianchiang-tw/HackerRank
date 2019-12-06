def find_runner_up( arr ):

    max_value = max( arr )

    # remove max_value
    while True:
        if max_value in arr:
            arr.remove( max_value )
        else:
            break

    #print("after cleaning:", arr )

    # get the runner_up
    runner_up = max( arr )

    return runner_up


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list( arr )
    runner_up = find_runner_up( arr )

    print( runner_up )
