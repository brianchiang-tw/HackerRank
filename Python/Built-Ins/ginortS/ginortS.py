# Enter your code here. Read input from STDIN. Print output to STDOUT

from functools import cmp_to_key

def even_odd(a, b):

    if a % 2 == 1 and b % 2 == 0:
        # even is larger than odd
        return -1

    elif a % 2 == 0 and b % 2 == 1:
        # even is larger than odd
        return 1

    else:
        # even, even is par
        # odd, odd is par
        # compare integer value
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0


def upper_lower(a, b):

    if a.isupper() and b.islower():
        # upper case is larger than lower case
        return 1

    elif a.islower() and b.isupper():
        return -1

    else:
        # upper, upper is par
        # lower, lower is par
        # compare ASCII value

        if ord(a) > ord(b):
            return 1
        elif ord(a) < ord(b):
            return -1
        else:
            return 0
        



def ginorts( a, b):

    '''
All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
    '''

    
    if a.isalpha() and b.isalpha():
        return upper_lower(a, b)

    elif a.isdigit() and b. isdigit():
        return even_odd( int(a), int(b) )

    elif a.isalpha() is False or b.isalpha() is False:

        if a.isdigit() and b.isalpha():
            # digit is larger than alphabet
            return 1

        elif a.isalpha() and b.isdigit():
            # digit is larger than alphabet
            return -1

if __name__ == '__main__':

    input_str = str( input() )

    # sort by customized rule and generate output string
    output_str = ''.join( sorted(input_str, key = cmp_to_key(ginorts) ) )

    print( output_str )
