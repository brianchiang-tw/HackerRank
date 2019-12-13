from math import erf

def normal_distribution_cdf( x, miu, sigma):

    z_score = ( x - miu )/ sigma

    cdf_of_x = ( 1 + erf( z_score / (2 ** 0.5) ) ) / 2

    return cdf_of_x



def to_percentage( ratio ):

    return ratio * 100.0



if __name__ == '__main__':

    max_ticket = 250
    num_of_student = 100
    avg_tck_per_student = 2.4
    std_tck_per_student = 2    

    avg_of_sample_sum = num_of_student * avg_tck_per_student
    std_of_sample_sum = (num_of_student ** 0.5) * std_tck_per_student

    under_limit = normal_distribution_cdf( max_ticket, avg_of_sample_sum, std_of_sample_sum)

    print( round(under_limit, 4) )