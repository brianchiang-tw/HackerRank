
def query_handler( _list_obj, query_entry ):


    command = query_entry[0]

    if "insert" == command:
        _list_obj.insert( int( query_entry[1] ), int( query_entry[2] ) )

    elif "print" == command:
        print(_list_obj)

    elif "remove" == command:
        _list_obj.remove( int( query_entry[1] ) )

    elif "append" == command:
        _list_obj.append( int( query_entry[1] ) )
    
    elif "sort" == command:
        _list_obj.sort()

    elif "pop" == command:
        _list_obj.pop(-1)
    
    elif "reverse" == command:
        _list_obj.reverse()


    return



if __name__ == '__main__':
    N = int(input())

    _list_obj = []

    for _ in range(N):
        
        query_entry = tuple( map( str, input().rstrip().split() ) )

        query_handler(_list_obj, query_entry)


