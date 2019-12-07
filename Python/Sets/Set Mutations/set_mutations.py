# Enter your code here. Read input from STDIN. Print output to STDOUT
class Query():

    def __init__(self, command, operand_set):

        self.command = command
        self.operand_set = operand_set


from typing import Set
def query_handler( set_a:Set, query_entry:Query ):

    if query_entry.command == "intersection_update":
        set_a.intersection_update( query_entry.operand_set )
    
    elif query_entry.command == "update":
        set_a.update( query_entry.operand_set )
    
    elif query_entry.command == "symmetric_difference_update":
        set_a.symmetric_difference_update( query_entry.operand_set )

    elif query_entry.command == "difference_update":
        set_a.difference_update( query_entry.operand_set )


    return


def sum_of_set( set_a:Set)->int:
    return sum( set_a )



if __name__ == '__main__':

    n, set_A = int( input() ), set( map(int, input().split() ) )
    num_of_query = int( input() )


    for _ in range( num_of_query ):

        input_str = input()
        command, len_of_operand = input_str.split()[0], int(input_str.split()[1])
        operand_set = set( map( int, input().split() ) )

        query_entry = Query( command, operand_set )

        # execute query entry
        query_handler(set_A, query_entry)



    print( sum_of_set(set_A) )