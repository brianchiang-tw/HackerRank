# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_palindromic( s ):

    return s[::] == s[::-1]


if __name__ == '__main__':

    n = int( input() )

    nums = list( map( int, input().split() ) )

    all_positive = all( ( x > 0 ) for x in nums  )

    any_palindromic = any( is_palindromic(str(x)) for x in nums )

    if all_positive and any_palindromic:
        print("True")
    else:
        print("False")


