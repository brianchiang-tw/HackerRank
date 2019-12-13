from math import erf

def normal_distribution_cdf( x, miu, sigma):

    z_score = ( x - miu )/ sigma

    cdf_of_x = ( 1 + erf( z_score / (2 ** 0.5) ) ) / 2

    return cdf_of_x



def to_percentage( ratio ):

    return ratio * 100.0



if __name__ == '__main__':

    max_weight = 9800
    num_of_boxes = 49
    avg_weight_of_box = 205
    std_weight_of_box = 15    

    avg_of_sample_sum = avg_weight_of_box * num_of_boxes
    std_of_sample_sum = (num_of_boxes ** 0.5) * std_weight_of_box

    under_limit = normal_distribution_cdf( max_weight, avg_of_sample_sum, std_of_sample_sum)

    print( round(under_limit, 4) )