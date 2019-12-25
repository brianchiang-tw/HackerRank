import numpy as np

if __name__ == '__main__':

    coef = list( map(float, input().split() ) )

    polynomial = np.poly1d( coef  ) 
    
    x = float( input() )

    print( np.polyval(polynomial, x) )



