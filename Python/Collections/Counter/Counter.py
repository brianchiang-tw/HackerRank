# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

def look_up_and_cashier( size_dict, size, price):

    payment = 0

    if size_dict[size] != 0:
        payment = price

        # number in stock decrease by 1, after selling one pair of shoes
        size_dict[size] -= 1
    else:
        pass

    return payment



if __name__ == '__main__':

    X = int( input() )
    shoe_size_in_warehouse = list( map(int, input().split() ) )

    size_dict = Counter(shoe_size_in_warehouse)

    N = int( input() )

    total_revenue = 0

    for _ in range(N):

        buf = list( map(int, input().split() ) )
        total_revenue += look_up_and_cashier( size_dict, size = buf[0], price = buf[1] )

    print( total_revenue ) 