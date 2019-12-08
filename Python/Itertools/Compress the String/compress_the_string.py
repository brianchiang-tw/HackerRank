# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

def compress_sequence( s:str )->None:

    # preprocessing, string(character) to int
    data = list( map(int, s))

    groups = []
    uniquekeys = []
    for k, g in groupby( data, lambda x: ( int(x) ) ):

        # Store group iterator as a list
        groups.append(list(g))    

        # Store unique key as a list
        uniquekeys.append(k)

    # output comparession pair: ( length of repetition, head element )
    for g in groups:
        print( tuple( (len(g), g[0]) ), end = ' ')

    return


if __name__ == '__main__':

    s = input()

    compress_sequence( s )