import re

regex = r'(?<=[^a-zA-Z_])([a-zA-Z_]*)(?=[^a-zA-Z_])'

pattern = re.compile( regex )

def find_occurrence( target, input_s):

    result = re.findall( pattern, input_s )

    return result.count( target )




if __name__ == '__main__':

    n = int( input() )

    input_list = []

    for _ in range(n):

        input_str = input()

        input_list.append( " " + input_str + " " )


    m = int( input() )

    for _ in range(m):

        target = input()

        sum_of_occ = 0
        for input_s in input_list:

            sum_of_occ += find_occurrence( target, input_s )

        print( sum_of_occ )