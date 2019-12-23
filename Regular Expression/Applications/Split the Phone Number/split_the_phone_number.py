import re

regex_phone_number = r'^([0-9]{1,3})(?:-|\s)([0-9]{1,3})(?:-|\s)([0-9]{4,10})$'

pattern = re.compile( regex_phone_number )

if __name__ == '__main__':

    n = int( input() )

    for _ in range(n):

        input_str = input() 

        match = re.match( pattern, input_str )

        print(f'CountryCode={match.group(1)},LocalAreaCode={match.group(2)},Number={match.group(3)}')

        # Example output
        # CountryCode=1,LocalAreaCode=877,Number=2638277