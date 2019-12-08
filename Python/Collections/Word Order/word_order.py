# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

if __name__ == '__main__':

    n = int( input() )

    # key : word
    # value : occurrence
    word_occ_dict = OrderedDict()

    for _ in range(n):

        word = input() 

        word_occ_dict[ word ] =  word_occ_dict.get( word, 0) + 1
        

    print( len(word_occ_dict) )
    
    for v in word_occ_dict.values():
        print( v, end = ' ')
