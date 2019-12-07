# Enter your code here. Read input from STDIN. Print output to STDOUT

from typing import Set

def add_element_to_set( set_a: Set, new_element:str)->None:

    set_a.add( new_element )

    return



def num_of_unique_element( set_a: Set)->int:

    return len(set_a)



if __name__ == '__main__':

    N = int( input() )

    set_a = set()

    for _ in range(N):
        input_str = input()
        add_element_to_set(set_a, input_str)
    
    
    print( num_of_unique_element( set_a ) )

