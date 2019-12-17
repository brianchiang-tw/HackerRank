import re

def validate_address( email ):

    regex = r'^<([A-Za-z0-9]+[A-Za-z0-9-\.\-_]*@[A-Za-z]+\.[A-Za-z]{1,3})>$'

    pattern = re.compile(regex)

    result = re.match( pattern, email )

    if result is None:
        return "Invalid"
    else:
        return "<" + result.group(1) + ">"


if __name__ == '__main__':

    n = int( input() )

    for _ in range(n):

        tokens = input().split()

        name, email = tokens[0], tokens[1]



        result = validate_address( email )

        if result == "Invalid":
            continue
        else:
            email = result

        print(f'{name} {email}')