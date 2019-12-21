
import re



if __name__ == '__main__':

    n = int( input() )

    input_list = []

    for _ in range(n):

        input_str = input()

        input_list.append( input_str )


    q = int( input() )

    for _dummy in range(q):


        target = input()

        count_of_substr = 0

        for input_s in input_list:

            pattern = r'(?<=[a-zA-Z0-9_]){}(?=[a-zA-Z0-9_])'.format( target )

            result = re.findall( pattern, input_s )

            count_of_substr += len( result )
        

        print( count_of_substr )


        
