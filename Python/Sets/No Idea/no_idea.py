# Enter your code here. Read input from STDIN. Print output to STDOUT
from typing import List, Set
def calc_happiness( nums: List, set_a:Set, set_b:Set)-> int:


    score_of_happiness = 0

    for x in nums:

        if x in set_a:
            score_of_happiness += 1
        
        if x in set_b:
            score_of_happiness -= 1

    return score_of_happiness



if __name__ == '__main__':

    n , m  = tuple( map( int, input().split() ) )

    nums = list( map( int, input().split() ) )

    set_a = set( map(int, input().split() ) )

    set_b = set( map(int, input().split() ) )

    score = calc_happiness( nums, set_a, set_b )

    print( score )