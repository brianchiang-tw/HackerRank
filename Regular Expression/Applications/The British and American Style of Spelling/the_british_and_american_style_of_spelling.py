import re

if __name__ == '__main__':

    n = int( input() )

    all_input = ""
    for _ in range(n):

        input_str = input()
        all_input += " " + input_str

    
    k = int( input() )

    for _ in range(k):

        query_str = input()

        regex = r'{}|{}'.format( query_str[:-2]+"se", query_str[:-2]+"ze" )

        pattern = re.compile(regex)

        result = re.findall( pattern, all_input)

        print( len(result) )