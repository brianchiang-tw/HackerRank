# Enter your code here. Read input from STDIN. Print output to STDOUT

class my_queue():

    def __init__( self ):

        self.inbox = []
        self.outbox = []



    def enqueue( self, value ):
        self.inbox.append( value )



    def dequeue( self):

        if len(self.outbox) != 0:
            # if outbox is not empty
            # then return and pop top of outbox
            return self.outbox.pop()


        else:
            # if outbox is empty
            # pop all element from inbox, and push into outbox, till inbox is empty
            # then return and pop top of outbox

            while len(self.inbox) != 0:

                top_of_inbox = self.inbox.pop(-1)
                self.outbox.append( top_of_inbox )


            return self.outbox.pop()         



    def front( self ):

        if len(self.outbox) != 0:
            # if outbox is not empty
            # then return top of outbox
            return self.outbox[-1]


        else:
            # if outbox is empty
            # pop all element from inbox, and push into outbox, till inbox is empty
            # then return top of outbox

            while len(self.inbox) != 0:

                top_of_inbox = self.inbox.pop(-1)
                self.outbox.append( top_of_inbox )


            return self.outbox[-1]   



def query_handler( query_list ):


    _queue = my_queue()

    for query_entry in query_list:

        if query_entry[0] == 1:

            # enqueue
            _queue.enqueue( query_entry[1] )

        elif query_entry[0] == 2:

            # dequeue
            _queue.dequeue()

        elif query_entry[0] == 3:

            # print the element on the head of queue
            print( _queue.front() )



if __name__ == '__main__':

    

    query_list = []

    number_of_query = int( input() )

    for _ in range( number_of_query ):

        query_entry = tuple( map(int, input().rstrip().split() ) )

        query_list.append( query_entry )


    query_handler( query_list )

    