def average(array):
    # your code goes here

    # pick up distinct elements from array
    set_of_distinct_height = set(array)

    # compute average from definition
    average = sum( set_of_distinct_height ) / len(set_of_distinct_height)

    return average



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)