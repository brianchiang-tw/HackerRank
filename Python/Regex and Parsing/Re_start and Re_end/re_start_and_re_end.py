import re

if __name__ == '__main__':

    input_str, token = input(), input()

    pattern = re.compile(token)
    result = pattern.search( input_str )

    if result is None:
        print("(-1, -1)")
    while result:

        # Note: python convetion is of tail exclusive notation
        print('({0}, {1})'.format( result.start(), result.end()-1 ) )
        result = pattern.search( input_str, result.start()+1 )
    
    

