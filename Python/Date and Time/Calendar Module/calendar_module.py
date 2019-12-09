# Enter your code here. Read input from STDIN. Print output to STDOUT

import time

def get_weekday( str_y_m_d):

    weekday = time.strftime("%A", time.strptime(str_y_m_d, "%Y-%m-%d")) 

    return weekday


if __name__ == '__main__':

    buf = list( input().split() )

    month, day, year = buf[0], buf[1], buf[2]

    date = [year, month, day]

    str_y_m_d = '-'.join( date )

    print( get_weekday( str_y_m_d ).upper() )