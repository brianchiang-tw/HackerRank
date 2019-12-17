
import re

def is_valid_phone_number( s )->str:

    regex = r'^([7-9]{1,1}[0-9]{9,9})$'

    pattern = re.compile( regex )

    result = re.match( pattern, s)

    if result is None:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':

    n = int( input() )

    for _ in range(n):

        phone_number = input()

        print( is_valid_phone_number(phone_number) )

        