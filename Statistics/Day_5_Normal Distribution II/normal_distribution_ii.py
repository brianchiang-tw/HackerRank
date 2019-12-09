# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import erf

def normal_distribution_cdf( x, miu, sigma):

    z_score = ( x - miu )/ sigma

    cdf_of_x = ( 1 + erf( z_score / (2 ** 0.5) ) ) / 2

    return cdf_of_x



def to_percentage( ratio ):

    return ratio * 100.0


miu, sigma = 70, 10

a = 80
less_than_a = normal_distribution_cdf( a, miu, sigma)

b = 60
less_than_b = normal_distribution_cdf( b, miu, sigma)


print( round( to_percentage(1.0-less_than_a), 2) )
print( round( to_percentage(1.0-less_than_b), 2) )
print( round( to_percentage(less_than_b), 2) )