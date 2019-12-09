# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

def can_plie_up( dequeue )->bool:

    prev_side = 2 ** 31
    while len(dequeue) != 0:

        if dequeue[0] > dequeue[-1]:
            # if left end is larger
            pick_up = dequeue.popleft()
            
        else:
            # if right end is larger
            pick_up = dequeue.pop()
            

        if pick_up <= prev_side:
            # valid pick up
            # update prev_side
            prev_side = pick_up
        
        else:
            # invalid pick up
            return "No"

    
    return "Yes"



if __name__ == '__main__':

    t = int( input() )

    for _ in range(t):
        n = int( input() )
        dequeue = deque( list( map(int, input().split() ) ) )
        print( can_plie_up(dequeue) )