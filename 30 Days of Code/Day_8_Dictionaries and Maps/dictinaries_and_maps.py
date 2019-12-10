# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if __name__ == '__main__':

    n = int( input() )

    name_phone_dict = dict()

    for i in range(n):

        tokens = input().split()
        name, phone = tokens[0], tokens[1]

        name_phone_dict[ name ] = phone


 
    
    for line_input in sys.stdin:


        name = line_input.strip()
        look_up = name_phone_dict.get( name, None)



        if look_up is not None:

            print( f'{name}={look_up}')
        
        else:
            print("Not found")

        


