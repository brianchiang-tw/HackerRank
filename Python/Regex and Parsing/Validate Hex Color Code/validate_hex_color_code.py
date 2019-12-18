import re

def print_color_code( line_str ):

    if '{' in line_str or '}' in line_str:
        return

    regex = r'#(?:[0-9a-fA-F]{3}){1,2}'

    pattern = re.compile(regex)

    colors = re.findall( pattern, line_str )

    

    if colors is not None:

        for color_code in colors:
            print( str(color_code) )

    return



if __name__ == '__main__':

    n = int( input() )

    search_flag = False

    for _ in range(n):

        try:
            input_str = input()
            if '{' in input_str:
                search_flag = True

            if '}' in input_str:
                search_flag = False
            

        except EOFError:
            #print( input_str )
            continue

        if search_flag:
            print_color_code( input_str )
