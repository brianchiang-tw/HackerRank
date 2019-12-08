# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

if __name__ == '__main__':

    n = int( input() )

    item_revenue = OrderedDict()

    for _ in range( n ):
        
        buf =  list( input().split() )
        price = int( buf[-1] )
        name = ' '.join( buf[:-1] )

        if name not in item_revenue:
            item_revenue[ name ] = price
        else:
            item_revenue[ name ] += price

    
    for name, revenue in item_revenue.items():

        print( f'{name} {revenue}' )