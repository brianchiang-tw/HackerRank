# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

regex = r'([a-zA-Z0-9-_\.]+@[a-zA-Z0-9-_\.]+\.[a-zA-Z0-9-_]{2,})'

pattern = re.compile( regex )


if __name__ == '__main__':

    addr_list = []

    n = int( input() )

    for _ in range(n):

        input_str = input()

        result = re.findall(pattern, input_str)

        addr_list += [ e for e in result if e not in addr_list]

    addr_list.sort()

    output_str = ';'.join(addr_list)

    print( output_str )
    
    



