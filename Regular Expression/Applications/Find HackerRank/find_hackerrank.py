import re

regex_start_end = r'^(hackerrank).*(\1)$|^hackerrank$'
regex_start = r'^hackerrank'
regex_end = r'.*(hackerrank)$'

pattern_start_end = re.compile( regex_start_end )
pattern_start = re.compile( regex_start )
pattern_end = re.compile( regex_end )


if __name__ == '__main__':

    n = int( input() )

    for _ in range( n ):

        input_str = input() 

        if re.match(pattern_start_end, input_str ):
            print("0")

        elif re.match(pattern_start, input_str):
            print("1")

        elif re.match(pattern_end, input_str):
            print("2")

        else:
            print("-1") 