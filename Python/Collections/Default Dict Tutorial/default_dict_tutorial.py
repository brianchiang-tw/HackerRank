# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

def loop_up_occurence_index( word_index_dict:defaultdict, word:str)->None:
    
    loop_up_result = word_index_dict[word]

    if len(loop_up_result) != 0 :
        print(' '.join( map(str, loop_up_result) ) )
    else:
        print(-1)
    
    return


if __name__ == '__main__':

    # key: string
    # value: list of occurrence index, index starts counting from 1
    word_index_dict = defaultdict( list )

    buf = list( map( int, input().split() ) )
    n, m = buf[0], buf[1]
    
    for occ_idx in range(n):

        word = input()
        
        # update occurrence index of word
        word_index_dict[word].append( occ_idx+1 )

    
    for _ in range( m ):

        word_of_look_up = input()
        loop_up_occurence_index( word_index_dict, word_of_look_up )
