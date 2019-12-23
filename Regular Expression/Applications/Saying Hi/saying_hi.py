import re

regex = r'^[Hh][Ii][ ][^Dd].*$'

pattern = re.compile( regex )

if __name__ == '__main__':

    n = int( input() )

    for _ in range( n ):

        input_str = input()

        if re.match(pattern, input_str):

            print( input_str )

        else:
            pass
            continue