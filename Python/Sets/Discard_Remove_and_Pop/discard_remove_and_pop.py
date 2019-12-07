from typing import Set

class Query():

    def __init__(self, params):
        self.command = params[0]

        if len(params) == 2:
            self.element = int(params[1])

    

def query_handler(set_a:Set, query:Query)->None:

    if query.command == "pop":
        set_a.pop()
    
    elif query.command == "remove":
        # remove: strict deletion
        set_a.remove( query.element )
    
    elif query.command == "discard":
        # discard: loose deletion
        set_a.discard( query.element )


    return


def sum_of_set( set_a:set)->int:

    return sum( set_a )



if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))

    query_length = int( input() )

    for _ in range( query_length ):
        query_entry = Query( tuple( input().split() ) )
        query_handler( s, query_entry)

    print( sum_of_set(s) )
