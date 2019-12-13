# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':

    regex = r'([a-zA-Z0-9])\1+'

    pattern = re.compile( regex )

    input_string = input()


    # catch repeated character
    result = re.search( r'([A-Za-z0-9])\1+', input_string)

    if result:
        print( result.group(1) )

    else:
        print( "-1" )

