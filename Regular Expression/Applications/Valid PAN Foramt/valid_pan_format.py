import re

regex = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'

pattern_for_PAN = re.compile( regex )

if __name__ == '__main__':

    n = int( input() )


    for _ in range( n ):

        input_str = input() 


        result = re.match( pattern_for_PAN, input_str )

        if result is not None:

            print("YES")

        else:

            print("NO") 