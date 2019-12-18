
import re


def validate_elements( s ):

    regex = r'^([a-zA-Z0-9]{10})$'

    pattern = re.compile( regex )

    result = re.match( pattern, s )

    if result is None:
        return False
    else:
        return True



'''

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits ( 0-9 ).
It should only contain alphanumeric characters ( a-z , A-Z  &  0-9 ).
No character should repeat.
There must be exactly  10 characters in a valid UID.

'''



def validate_occurrence( s:str, opcode ):

    if opcode == "uppercase":

        return len( list(filter( lambda x:x.isupper(), s) ) )
    
    elif opcode == "digits":

        return len( list( filter( lambda x:x.isdigit(), s) ) )

    elif opcode == "distint":

        return len(s) == len( set(s) )



if __name__ == '__main__':

    n = int( input() )

    for _ in range(n):

        uid = input()

        if  validate_elements(uid) and \
            validate_occurrence(uid, "uppercase") >= 2 and \
            validate_occurrence(uid, "digits") >= 3 and \
            validate_occurrence(uid, "distint"):

            print("Valid")

        else:

            print("Invalid") 

