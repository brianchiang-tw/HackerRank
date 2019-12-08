# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':

    n = int( input() )
    index_of_marks = list( input().split() ).index("MARKS")

    sum_val = 0
    for _ in range(n):
        sum_val += int( list( input().split() )[ index_of_marks ] )

    print( round(sum_val/n, 2) )