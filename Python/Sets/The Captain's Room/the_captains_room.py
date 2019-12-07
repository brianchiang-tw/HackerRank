from typing import List
from collections import Counter

def find_captains_room( onboard_list:List, k:int)->int:

    serial_occ_dict = Counter( onboard_list )

    for serial, occ in serial_occ_dict.items():

        if occ != k:
            return serial

    return -1

# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':

    k, onboard_list = int( input() ), list( map(int, input().split() ) )

    print( find_captains_room(onboard_list, k) ) 
