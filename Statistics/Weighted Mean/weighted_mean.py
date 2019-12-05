# Enter your code here. Read input from STDIN. Print output to STDOUT
from typing import List

def get_weighted_mean( nums:List[int], weight: List[int] )->float:

    weighted_sum = 0;

    for i in range(len(nums)):

        weighted_sum += nums[i] * weight[i]

    
    weighted_mean = weighted_sum / sum(weight)

    print( "%.1f" % weighted_mean)


    return



if __name__ == '__main__':

    length_of_arr = int( input() )

    arr_of_number = list( map(int, input().split() ) )

    arr_of_weight = list( map(int, input().split() ) )

    get_weighted_mean( arr_of_number, arr_of_weight)
