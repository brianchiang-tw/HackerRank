


def stack_operation( query_queue ):

    _stack = []

    max_of_stack = 0
    while( len(query_queue) != 0) :

        # pop and execute one query from query_queue
        query = query_queue.pop(0)

        if 1 == query[0]:
            # push
            _stack.append( query[1] )

            # update max of stack
            if( query[1] > max_of_stack ):
                max_of_stack = query[1]

        elif 2 == query[0]:
            # pop
            pop_element = _stack.pop()

            if( pop_element == max_of_stack ):

                if len(_stack) > 0 :

                    # update max of stack
                    max_of_stack = max( _stack )
                else:
                    # stack is empty, reset max_of_stack to 0
                    max_of_stack = 0


        else:
            # print the max element of stack
            #print( max(_stack) )
            print( max_of_stack )



    return





# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':

    query_count = int( input() )

    query_list = []

    for i in range( query_count ):

        query_entry = tuple( map( int, input().split() ) )

        query_list.append( query_entry ) 

    stack_operation( query_list )
