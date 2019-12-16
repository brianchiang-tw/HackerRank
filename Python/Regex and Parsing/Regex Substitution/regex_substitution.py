# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

#Squaring numbers
def logic_symbol(match):

    token = match.group()

    if  token == '&&':
        return "and"
    elif token == "||":
        return "or"


if __name__ == '__main__':

    N = int( input() )

    for _ in range( N ):

        input_str = input()

        # to match ' && ' or ' || '
        regex = r'((?<=[ ])(&&)(?=[ ]))|((?<=[ ])(\|\|)(?=[ ]))'
        print( re.sub(regex, logic_symbol, input_str) )


    
