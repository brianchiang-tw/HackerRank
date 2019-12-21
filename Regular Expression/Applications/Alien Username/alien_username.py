import re

def validate_username( s ):

    regex = r'^(_|\.)[0-9]+[a-zA-Z]*(_?)$'

    pattern = re.compile( regex )

    result = re.match( pattern, s)

    if result is None:
        return False

    else:
        return True



if __name__ == '__main__':

    n = int( input() )

    for _ in range( n ):

        input_str = input()

        if validate_username(input_str):
            print("VALID")
        
        else:
            print("INVALID")