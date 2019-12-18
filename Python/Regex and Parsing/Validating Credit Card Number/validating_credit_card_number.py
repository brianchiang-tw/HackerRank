import re

def validate_card_number( s ):

    regex = r'^([4-6][0-9]{3}\-?)([0-9]{4}\-?){3}$'
    pattern = re.compile( regex )

    result = re.match(pattern, s)

    if result is None:
        # fit general form of credit card or not
        return False


    # remove all the dash '-' in string s for checking consecutive numbers
    s = s.replace('-', '')


    regex = r'([0-9])\1{3,}'
    pattern = re.compile( regex )

    result = re.search(pattern, s)

    if result is not None:
        # if consecutive number over four times
        return False

    
    return True


if __name__ == '__main__':

    n = int( input() )

    for _ in range(n):

        input_str = input()

        if validate_card_number( input_str ):
            print("Valid")
        else:
            print("Invalid")