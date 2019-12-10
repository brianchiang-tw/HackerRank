# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

if __name__ == '__main__':

    n = int( input() )

    for _ in range(n):

        input_str = input()

        try:
            re.compile( input_str )
            print("True")
            
        except re.error:
            print("False")
