import re

regex = r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$'

# The string must begin with between 0-3 (inclusive) lowercase letters.
# Immediately following the letters, there must be a sequence of digits (0-9). The length of this segment must be between 2 and 8, both inclusive.
# Immediately following the numbers, there must be atleast 3 uppercase letters.

pattern = re.compile( regex )

if __name__ == '__main__':

    n = int( input() )

    for _ in range( n ):

        input_str = input() 

        result = re.match(pattern, input_str)

        if result is not None:
            print("VALID")
        else:
            print("INVALID")