# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
from collections import deque

Query = namedtuple('Query', ['command','operand'])

def query_hanlder( query_entry:Query, dequeue:deque):

    if query_entry.command == "append":
        dequeue.append( query_entry.operand )

    elif query_entry.command == "pop":
        dequeue.pop()
    
    elif query_entry.command == "popleft":
        dequeue.popleft()
    
    elif query_entry.command == "appendleft":
        dequeue.appendleft( query_entry.operand )

    return


if __name__ == '__main__':

    dequeue = deque()

    n = int( input() )

    for _ in range( n ):

        buf = list( input().split() )
        
        if len(buf) == 1:
            query_entry = Query( buf[0], None)
        elif len(buf) == 2:
            query_entry = Query( buf[0], int(buf[1]) )

        query_hanlder( query_entry, dequeue)


    for x in dequeue:
        print(x, end = ' ')