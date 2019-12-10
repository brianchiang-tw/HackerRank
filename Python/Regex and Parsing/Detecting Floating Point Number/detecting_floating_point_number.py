# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':

    # sign of minus or positive is optional.
    # leading part with 0~9 is optional.
    # decimal point '.' is a must
    # trailing part with 0~9 has at least one digit width
    # Pure integer is not allowed.
    regex_for_floating = '^[+-]?[0-9]*\.[0-9]+$'
    
    n = int( input() )

    for _ in range( n ):

        s = input()

        if re.match(regex_for_floating, s):
            print("True")
        else:
            print("False")
