# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import erf

def normal_distribution_cdf( x, miu, sigma):

    z_score = ( x - miu )/ sigma

    cdf_of_x = ( 1 + erf( z_score / (2 ** 0.5) ) ) / 2

    return cdf_of_x


miu, sigma = 20, 2

a = 19.5
less_than_a = normal_distribution_cdf( a, miu, sigma)

b = 20
less_than_b = normal_distribution_cdf( b, miu, sigma)

c = 22
less_than_c = normal_distribution_cdf( c, miu, sigma)

between_b_and_c = less_than_c - less_than_b


print( round(less_than_a, 3) )
print( round(between_b_and_c, 3) )