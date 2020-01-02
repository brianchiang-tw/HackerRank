# Enter your code here. Read input from STDIN. Print output to STDOUT

def even_odd( s:str)->None:

    # print character with even index
    print(s[0::2], end='')

    # print whitespace
    print(' ', end = '')

    # print character with odd index, end symbol is new line \n
    print(s[1::2], end='\n')

    return


if __name__ == '__main__':

    t = int( input() )

    for _ in range(t):

        even_odd( input() )


